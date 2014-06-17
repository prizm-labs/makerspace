# -*- coding: utf-8 -*-
# handle Non-ASCII characters
# http://stackoverflow.com/questions/18078851/syntaxerror-of-non-ascii-character

from . import app

from . import db
import models

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

#from . import lm, oid
from flask.ext.login import login_user, logout_user, current_user, login_required
#from models import User, ROLE_USER, ROLE_ADMIN

#session = db.create_scoped_session()
# mysql://admin:admin@127.0.0.1:



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
@app.route('/register', methods=['POST'])
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

@app.route('/new_subscription', methods=['POST'])
def new_subscription():
    print request.query_string
    print request.args
    name = request.args.get('name')
    email = request.args.get('email')

    interface = AWeberInterface()
    _list = interface.find_list()
    subscriber = {
        'name': name,
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


@app.route('/')
def index():

    projects = db.session.query(models.Project).all()

    project_buckets = get_top_projects(projects)

    project_buckets['all'] = projects
    #TODO make sure all buckets have unique videos

    context_dict = project_buckets

    return render_template('_home.html', **context_dict)


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

        sub_text = '100% FREE. I promise never to spam you.'

        context_dict = {
            'project': project,
            'comment_form': forms.BlogCommentForm(),
            'subscribe_form': forms.SubscribeForm(),
            'suggested_projects': suggested_projects,
            'next_project': next_project,

            #adding from from subscribe page
            'form': forms.SubscribeForm(),
            'modal_title':'My best content on DIY, lifehacks, and pranks',
            'modal_subtitle':'Lifehack tips & videos delivered to you for free every week.',
            'form_text': 'This content will be life-changing. I promise.',
            'form_sub_text': sub_text.format(), 
            'call_to_action':'Get more videos & tips!'
            # http://stackoverflow.com/questions/10678229/selectively-escape-percent-in-python
            #'html': u"<h1>Contact the King</h1><p>I get tons of emails every day. While I can’t respond to every email, I do read all of them -- so please email away.</p><p>My email is grant at thekingofrandom dot com</p>"
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


@app.route('/contact')
def page_contact():
    # based on page_contact3.html
    context_dict = {
            'form': forms.ContactForm(),
            'html': u"<h1>Contact the King</h1><p>I get tons of emails every day. While I can’t respond to every email, I do read all of them -- so please email away.</p><p>My email is grant at thekingofrandom dot com</p>",
            'links': [
                { 'class':'email', 'title':'Email', 'url':'mailto:grant@thekingofrandom.com'},
                { 'class':'facebook', 'title':'Facebook', 'url':'https://www.facebook.com/thekingofrandomfanpage'},
                { 'class':'youtube', 'title':'Youtube','url':'https://www.youtube.com/user/01032010814'},
                { 'class':'twitter', 'title':'Twitter','url':'http://www.pinterest.com/thekingofrandom/random-weekend-projects/'},
                { 'class':'google-plus', 'title':'Google','url':'https://plus.google.com/u/0/+Thekingofrandom/posts'}
            ]
        }
    return render_template('_contact.html', **context_dict)

@app.route('/subscribe')
def page_subscribe():

    sub_text = '100% FREE. I promise never to spam you.'

    context_dict = {
            'form': forms.SubscribeForm(),
            'title':'My best content on DIY, lifehacks, and pranks',
            'subtitle':'Lifehack tips & videos delivered to you for free every week.',
            'form_text': 'This content will be life-changing. I promise.',
            'form_sub_text': sub_text.format(), 
            'call_to_action':'Get more videos & tips!'
            # http://stackoverflow.com/questions/10678229/selectively-escape-percent-in-python
            #'html': u"<h1>Contact the King</h1><p>I get tons of emails every day. While I can’t respond to every email, I do read all of them -- so please email away.</p><p>My email is grant at thekingofrandom dot com</p>"
            }


    return render_template('_subscribe.html', **context_dict)


'''
@app.route('/page/<slug>')
def show_page(slug):
    context_dict = {
            'category': tag.name.capitalize(),
            'projects': projects
        }

    return render_template('_category.html', **context_dict)
'''

    



