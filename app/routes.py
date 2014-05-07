from . import app

from . import db, models
from sqlalchemy import func,desc
from collections import OrderedDict
import random

from flask import render_template, request, jsonify, flash, redirect, session, url_for, g
import nav_menu

import forms
from aweber_api import AWeberAPI
from aweber import AWeberInterface

from flask.ext.mail import Message
from . import mail
from config import ADMINS

from . import lm, oid
from flask.ext.login import login_user, logout_user, current_user, login_required
#from models import User, ROLE_USER, ROLE_ADMIN

#session = db.create_scoped_session()
# mysql://admin:admin@127.0.0.1:

@lm.user_loader
def load_user(id):
    return db.session.query(models.User).get(int(id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    print g.user
    if g.user is not None and g.user.is_authenticated():
        if g.user.role == models.ROLE_ADMIN:
            return redirect('/admin')
        else:
            return redirect('/')

    form = forms.OpenIdLoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('_login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = db.session.query(models.User).filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = models.User(nickname = nickname, email = resp.email, role = models.ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)

    #return redirect(request.args.get('next') or url_for('index'))
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))




# Adding a filter for formatting date
@app.template_filter('format_date')
def _jinja2_format_date(date, format_=None):
    """
    Takes datetime/date object and eturns strings in format of `Jul 9, 2013` and `Jan 23, 2014`.
    format_ param can be passed for specifying custom format.
    """
    return date.strftime(format_ or '%b %d, %Y')


# Enabling `do` extension to mitigate scoping issues
# Was unable to access `active` variable inside nested for and if blocks in `_header.html`
# http://stackoverflow.com/questions/17925674
app.jinja_env.add_extension('jinja2.ext.do')

# Pushing zip function to jinja global namespace
app.jinja_env.globals.update(zip=zip)

def projects_with_tag(tag_obj):
    tagged_projects = []
    projects = db.session.query(models.tags).filter(models.tags.c.tag_id==tag_obj.id).all()

    for mapping in projects:
        tagged_projects.append(mapping.project_id)

    return tagged_projects

def projects_with_ids(ids_list):
    return db.session.query(models.Project).filter(models.Project.id.in_(ids_list)).all()

def get_page_views(project):
    page_views = project.metas[0].data['page_views']
    page_views = int(page_views)
    return page_views

def get_featured(projects):
    featured_tag_id = 55

    featured_projects = [i for i in projects if any(t.id == featured_tag_id for t in i.tags)]

    '''
    featured_tag = db.session.query(models.Tag).filter(models.Tag.id==featured_tag_id).first()
    featured_projects = projects_with_tag(featured_tag)
    print 'featured projects ids:'
    print featured_projects
    featured_projects = projects_with_ids(featured_projects)
    '''
    return featured_projects


def compare_page_views(projectA, projectB):
    a = get_page_views(projectA)
    b = get_page_views(projectB)
    if a > b:
        return -1
    elif a < b:
        return 1
    else:
        return 0


def get_top_projects(projects,asIds = False):

    bucket_limit = 3

    #latest = db.session.query(models.Project).order_by(models.Project.created_on.desc()).limit(bucket_limit).all()
    latest = sorted(projects, key=lambda project: project.created_on)
    latest = latest[::-1]
    latest = latest[:bucket_limit]
    
    popular = sorted(projects, cmp=compare_page_views)
    popular = popular[:bucket_limit]
    
    featured = get_featured(projects)
    featured = featured[:bucket_limit]

    print 'latest projects:'
    for p in latest:
        print p.title

    print 'popular projects:'
    for p in popular:
        print p.title
        print get_page_views(p)

    print 'featured projects:'
    for p in featured:
        print p.title

    def mapId(project):
        return project.id

    if (asIds):
        latest = map(mapId,latest)
        popular = map(mapId,popular)
        featured = map(mapId,featured)

    return { 'latest':latest, 'popular':popular, 'featured':featured }


# Injecting newsletter form and navigation menu dicts into the template context
@app.context_processor
def inject_globals():
    return dict(
        newsletter_form=forms.NewsletterSubscriptionForm(),
        header_nav=nav_menu.header_nav,
        sidebar_nav=nav_menu.sidebar_nav
    )

# Routing
#http://flask.pocoo.org/docs/api/#url-route-registrations


# API Routes

# http://0.0.0.0:7777/register?email=michael.a.garrido%40gmail.com
@app.route('/register')
def email_register():
    print request.query_string
    print request.args
    email = request.args.get('email')

    interface = AWeberInterface()
    _list = interface.find_list()
    subscriber = {
        'email': email
    }
    response = interface.add_subscriber(subscriber, _list)
    print response

    return jsonify(response)

@app.route('/contact_message', methods=['POST'])
def contact_email():

    success = False
    data = ''
    print request.form

    # validate crsf token 
    # http://wtforms.simplecodes.com/docs/1.0.2/ext.html

    form = forms.ContactForm(request.form)

    if form.validate():
        #pass # We're all good, create a user or whatever it is you do
        

        email = request.form['email']
        name = request.form['name'] or 'Anonymous'
        message = request.form['message']

        msg = Message('Contact form: '+email, sender = ADMINS[0], recipients = ADMINS)
        msg.body = 'Name: '+name+', Email: '+email+', Message: '+message
        msg.html = 'Name: '+name+', Email: '+email+', Message: '+message

        with app.app_context():
            mail.send(msg)

        success = True
        data = 'Thanks, I will contact you soon!'
    elif form.csrf_token.errors:
        data = 'Invalid token'
        #pass # If we're here we suspect the user of cross-site request forgery
    else:
        #pass # Any other errors
        data = 'Unknown error'

    response = { 'success': success, 'data': data }
    print response

    return jsonify(response)
'''
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS
msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
  mail.send(msg)
'''


# Page Routes

@app.route('/')
def index():

    projects = db.session.query(models.Project).all()

    top_projects = get_top_projects(projects)


    #TODO make sure all buckets have unique videos

    context_dict = top_projects

    return render_template('_home.html', **context_dict)


# standalone content pages
def standalone_content(page):

    context_dict = {
            'title': page.title,
            'html':page.html
    }

    return render_template('_standalone.html', **context_dict)


from functools import partial

pages = db.session.query(models.Page).all()

for page in pages:
    app.add_url_rule('/'+page.slug, 
        page.slug, # this is the name used for url_for
        #standalone_content(page))
        partial(standalone_content, page=page))

    # TODO register slugs with base template (i.e. footer), so other pages can link with url_for    
    # http://stackoverflow.com/questions/14342969/python-flask-route-with-dynamic-first-component



@app.route('/project/<slug>')
def show_project(slug):

    project = db.session.query(models.Project).filter(models.Project.slug == slug).first()
    projects = db.session.query(models.Project).all()

    if (project == None):
        render_template('_index.html')
    else:
        suggested_projects = []
        next_project = []
        
        # Get suggested projects by tag
        # http://stackoverflow.com/questions/3618690/how-to-query-a-table-in-sqlalchemy
        # http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html
        for tag in project.tags:
            suggested_projects.extend(projects_with_tag(tag))


        top_projects = get_top_projects(projects,True)

        suggested_projects += top_projects['featured']+top_projects['latest']+top_projects['popular']

        # https://docs.python.org/3/library/collections.html#collections.OrderedDict
        suggested_projects = list(OrderedDict.fromkeys(suggested_projects))

        # remove current project from suggestions
        if project.id in suggested_projects:
            print 'found same project in suggestions'
            suggested_projects.remove(project.id)

        # http://stackoverflow.com/questions/444475/sqlalchemy-turning-a-list-of-ids-to-a-list-of-objects
        suggested_projects = projects_with_ids(suggested_projects)

        random.shuffle(suggested_projects)

        next_project = suggested_projects[0]
        suggested_projects = suggested_projects[1:4]


        #TODO do not show 'featured' tag

        context_dict = {
            'project': project,
            'comment_form': forms.BlogCommentForm(),
            'subscribe_form': forms.SubscribeForm(),
            'suggested_projects': suggested_projects,
            'next_project': next_project
        }

        # record view count
        # http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#sqlalchemy.dialects.postgresql.HSTORE

        page_views = project.metas[0].data['page_views']
        page_views = int(page_views)
        page_views+=1

        project.metas[0].data['page_views'] = str(page_views)

        print 'project page views:'+str(page_views)
        
        db.session.commit()

        return render_template('_project.html', **context_dict)
        # template based on blog_item_option1


@app.route('/category/<slug>')
def show_category(slug):
    # http://stackoverflow.com/questions/16573095/case-insensitive-flask-sqlalchemy-query
    tag = db.session.query(models.Tag).filter(func.lower(models.Tag.name) == func.lower(slug)).first()

    #print tag

    if (tag == None):
        return render_template('_index.html')
    else:
        projects = projects_with_tag(tag)
        projects = projects_with_ids(projects)

        context_dict = {
            'category': tag.name.capitalize(),
            'projects': projects
        }

        return render_template('_category.html', **context_dict)


@app.route('/page/<slug>')
def show_page(slug):
    context_dict = {
            'category': tag.name.capitalize(),
            'projects': projects
        }

    return render_template('_category.html', **context_dict)

@app.route('/contact')
def page_contact():
    # based on page_contact3.html
    return render_template('_contact.html', form=forms.ContactForm())



    



