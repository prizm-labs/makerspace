"""
Following blocks are available in the templates.

css             - Use this for placing page specific styles.
main_content    - Use this for main content area.
js              - Use this for placing page specific scripts.
js_lt_ie9       - Use this for placing scripts inside `less than ie9` conditional


Use the `page_title` variable to set the page's title. Like -
    {% set page_title = "Unify - Personal Profile" %}


Set the following flags to enable/disable certain parts of the site.

breadcrumbs                         - To enable breadcrumbs, set this to `True`.
disable_breadcrumb_bottom_margin    - To remove breadcrumb sections's bottom margin,
                                      set this to true
disable_header                      - To disable header, set this to `True`.
disable_footer                      - To disable footer, set this to `True`.

E.g.
    {% set breadcrumbs = True %}


`format_date` filter has been added to the jinja context which can used to format a
datetime object to produce date string like `Fri, 01 Jan.` and `Thu, Feb 6.`.
"""

from flask import Flask
from flask import request, jsonify

from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:password@127.0.0.1/makefoo'

db = SQLAlchemy(app)
babel = Babel(app)

import models

import routes

'''
session = db.create_scoped_session()

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
    projects = session.query(models.tags).filter(models.tags.c.tag_id==tag_obj.id).all()

    for mapping in projects:
        tagged_projects.append(mapping.project_id)

    return tagged_projects

def projects_with_ids(ids_list):
    return session.query(models.Project).filter(models.Project.id.in_(ids_list)).all()

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



@app.route('/project/<slug>')
def show_project(slug):
    project = models.Project.query.filter(models.Project.slug == slug).first()

    if (project == None):
        render_template('index.html')
    else:

        suggested_projects = []
        next_project = []
        
        # Get suggested projects by tag
        # http://stackoverflow.com/questions/3618690/how-to-query-a-table-in-sqlalchemy
        # http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html
        for tag in project.tags:
            suggested_projects.extend(projects_with_tag(tag))

        # https://docs.python.org/3/library/collections.html#collections.OrderedDict
        suggested_projects = list(OrderedDict.fromkeys(suggested_projects))

        # http://stackoverflow.com/questions/444475/sqlalchemy-turning-a-list-of-ids-to-a-list-of-objects
        suggested_projects = projects_with_ids(suggested_projects)
        random.shuffle(suggested_projects)

        next_project = suggested_projects[0]
        suggested_projects = suggested_projects[1:4]

        #TODO
        # Get suggested projects by related_project

        #TODO
        # Get suggested projects by popularity/views

        #TODO do not show 'featured' tag

        context_dict = {
            'project': project,
            'blog_post': sample_data.blog_posts[0],
            'comments': sample_data.comments,
            'comment_form': forms.BlogCommentForm(),
            'suggested_projects': suggested_projects,
            'subscribe_form': forms.SubscribeForm(),
            'next_project': next_project
        }

        return render_template('project.html', **context_dict)
        # template based on blog_item_option1


@app.route('/category/<slug>')
def show_category(slug):
    # http://stackoverflow.com/questions/16573095/case-insensitive-flask-sqlalchemy-query
    tag = models.Tag.query.filter(func.lower(models.Tag.name) == func.lower(slug)).first()

    print tag

    if (tag == None):
        return render_template('index.html')
    else:
        projects = projects_with_tag(tag)
        projects = projects_with_ids(projects)

        context_dict = {
            'category': tag.name.capitalize(),
            'projects': projects
        }

        return render_template('category.html', **context_dict)
    

@app.route('/')
def index():
    return render_template('index.html')
    # lastest
    # now
    # time range
    # query for projects sorted by post date

    # popular
    # query for projects sorted by view count

    # featured
    # query for projects with tag 'featured'
'''