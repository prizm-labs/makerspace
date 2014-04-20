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

from flask import Flask, render_template
from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy
import sample_data
import forms
import nav_menu

from collections import OrderedDict
import random
from sqlalchemy import func


app = Flask(__name__)
app.secret_key = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:password@127.0.0.1/makefoo'

db = SQLAlchemy(app)
babel = Babel(app)

#from . import models
import models

session = db.create_scoped_session()

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


@app.route('/page_home1')
def page_home1():
    return render_template('page_home1.html')


@app.route('/page_home2')
def page_home2():
    return render_template('page_home2.html')


@app.route('/page_home3')
def page_home3():
    return render_template('page_home3.html')


@app.route('/page_home4')
def page_home4():
    return render_template('page_home4.html')


@app.route('/page_home5')
def page_home5():
    return render_template('page_home5.html')


@app.route('/page_home6')
def page_home6():
    return render_template('page_home6.html')


@app.route('/page_home7')
def page_home7():
    return render_template('page_home7.html')


@app.route('/page_about')
def page_about():
    return render_template('page_about.html')


@app.route('/page_about1')
def page_about1():
    return render_template('page_about1.html')


@app.route('/page_services')
def page_services():
    return render_template('page_services.html')


@app.route('/page_services1')
def page_services1():
    return render_template('page_services1.html')


@app.route('/page_pricing')
def page_pricing():
    return render_template('page_pricing.html')


@app.route('/page_invoice')
def page_invoice():
    return render_template('page_invoice.html', invoice=sample_data.invoice)


@app.route('/page_meet_our_team')
def page_meet_our_team():
    return render_template('page_meet_our_team.html')


@app.route('/page_coming_soon')
def page_coming_soon():
    return render_template('page_coming_soon.html')


@app.route('/page_faq')
def page_faq():
    return render_template('page_faq.html')


@app.route('/page_funny_boxes')
def page_funny_boxes():
    return render_template('page_funny_boxes.html')


@app.route('/page_gallery')
def page_gallery():
    return render_template('page_gallery.html')


@app.route('/page_registration')
def page_registration():
    return render_template('page_registration.html', form=forms.RegisterForm())


@app.route('/page_registration1')
def page_registration1():
    return render_template('page_registration1.html', form=forms.RegisterForm())


@app.route('/page_login')
def page_login():
    return render_template('page_login.html', form=forms.LoginForm())


@app.route('/page_login1')
def page_login1():
    return render_template('page_login1.html', form=forms.LoginForm())


@app.route('/page_404_error')
def page_404_error():
    return render_template('page_404_error.html')


@app.route('/page_404_error1')
def page_404_error1():
    return render_template('page_404_error1.html')


@app.route('/page_clients')
def page_clients():
    return render_template('page_clients.html')


@app.route('/page_privacy')
def page_privacy():
    return render_template('page_privacy.html')


@app.route('/page_terms')
def page_terms():
    return render_template('page_terms.html')


@app.route('/page_2_columns_left')
def page_2_columns_left():
    return render_template('page_2_columns_left.html')


@app.route('/page_2_columns_right')
def page_2_columns_right():
    return render_template('page_2_columns_right.html')


@app.route('/page_3_columns')
def page_3_columns():
    return render_template('page_3_columns.html')


@app.route('/feature_grid')
def feature_grid():
    return render_template('feature_grid.html')


@app.route('/feature_boxes')
def feature_boxes():
    return render_template('feature_boxes.html')


@app.route('/feature_typography')
def feature_typography():
    return render_template('feature_typography.html')


@app.route('/feature_tagline_boxes')
def feature_tagline_boxes():
    return render_template('feature_tagline_boxes.html')


@app.route('/feature_buttons')
def feature_buttons():
    return render_template('feature_buttons.html')


@app.route('/feature_icons')
def feature_icons():
    return render_template('feature_icons.html')


@app.route('/feature_thumbnails')
def feature_thumbnails():
    return render_template('feature_thumbnails.html')


@app.route('/feature_components')
def feature_components():
    return render_template('feature_components.html')


@app.route('/feature_accordion_and_tabs')
def feature_accordion_and_tabs():
    return render_template('feature_accordion_and_tabs.html')


@app.route('/feature_navigations')
def feature_navigations():
    return render_template('feature_navigations.html')


@app.route('/feature_tables')
def feature_tables():
    return render_template('feature_tables.html', users=sample_data.users)


@app.route('/feature_forms')
def feature_forms():
    return render_template('feature_forms.html', form=forms.LoginForm())


@app.route('/feature_testimonials')
def feature_testimonials():
    return render_template('feature_testimonials.html')


@app.route('/portfolio_text_blocks')
def portfolio_text_blocks():
    return render_template('portfolio_text_blocks.html')


@app.route('/portfolio_2_column')
def portfolio_2_column():
    return render_template('portfolio_2_column.html')


@app.route('/portfolio_3_column')
def portfolio_3_column():
    return render_template('portfolio_3_column.html')


@app.route('/portfolio_4_column')
def portfolio_4_column():
    return render_template('portfolio_4_column.html')


@app.route('/portfolio_item')
def portfolio_item():
    return render_template('portfolio_item.html')


@app.route('/portfolio_item1')
def portfolio_item1():
    return render_template('portfolio_item1.html')


@app.route('/page_contact1')
def page_contact1():
    return render_template('page_contact1.html', form=forms.ContactForm())


@app.route('/page_contact2')
def page_contact2():
    return render_template('page_contact2.html', form=forms.ContactForm())


@app.route('/page_contact3')
def page_contact3():
    return render_template('page_contact3.html', form=forms.ContactForm())


@app.route('/blog_page')
def blog_page():
    return render_template('blog_page.html')


@app.route('/blog_large')
def blog_large():
    context_dict = {
        'blog_posts': sample_data.blog_posts[:3],
        'tags': sample_data.tags,
    }
    return render_template('blog_large.html', **context_dict)


@app.route('/blog_medium')
def blog_medium():
    context_dict = {
        'blog_posts': sample_data.blog_posts[3:7],
        'tags': sample_data.tags,
    }
    return render_template('blog_medium.html', **context_dict)


@app.route('/blog_full_width')
def blog_full_width():
    context_dict = {
        'blog_posts': sample_data.blog_posts[7:],
        'tags': sample_data.tags,
    }
    return render_template('blog_full_width.html', **context_dict)


@app.route('/blog_left_sidebar')
def blog_left_sidebar():
    context_dict = {
        'blog_posts': sample_data.blog_posts2,
    }
    return render_template('blog_left_sidebar.html', **context_dict)


@app.route('/blog_right_sidebar')
def blog_right_sidebar():
    context_dict = {
        'blog_posts': sample_data.blog_posts2,
    }
    return render_template('blog_right_sidebar.html', **context_dict)


@app.route('/blog_item_option1')
def blog_item_option1():
    context_dict = {
        'blog_post': sample_data.blog_posts[0],
        'comments': sample_data.comments,
        'comment_form': forms.BlogCommentForm(),
    }
    return render_template('blog_item_option1.html', **context_dict)


@app.route('/blog_item_option2')
def blog_item_option2():
    context_dict = {
        'blog_post': sample_data.blog_posts[7],
        'comments': sample_data.comments,
        'comment_form': forms.BlogCommentForm(),
    }
    return render_template('blog_item_option2.html', **context_dict)
