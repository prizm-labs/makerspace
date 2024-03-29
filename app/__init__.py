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

from flask import Flask, request, jsonify

import os
from flask.ext.openid import OpenID
from config import basedir

from flask.ext.assets import Environment, Bundle

from flask.ext.admin import Admin
from flask.ext import login

from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.mail import Mail

from flask_s3 import FlaskS3
from flask.ext.compress import Compress

# server robots.txt at root
# http://www.robotstxt.org/orig.html
# https://vilimpoc.org/blog/2012/11/21/serving-static-files-from-root-and-not-static-using-flask/
app = Flask(__name__,static_url_path='')
app.config.from_object('config')

# custom Jinja template prefix
# http://flask.pocoo.org/snippets/101/
app.jinja_env.line_statement_prefix = '%'

db = SQLAlchemy(app)
babel = Babel(app)

# custom fonts: Mueso Sans
# https://typekit.com/fonts/museo-sans

assets = Environment(app)
sass = Bundle('sass/master.sass', filters='sass', output='gen/sass.css', depends='sass/*.sass')
assets.register('sass_all',sass)

s3 = FlaskS3(app)
compress = Compress(app)

# http://stackoverflow.com/questions/16826233/why-wont-python-webassets-pyscss-regenerate-css-from-scss-files-in-debug-mode
# https://github.com/miracle2k/webassets/issues/231

mail = Mail(app)

'''
sass = Bundle('*.sass' filters='sass', output='gen/sass.css')
all_css = Bundle('css/jquery.calendar.css', sass,
                 filters='cssmin', output="gen/all.css")
{% assets "js_all" %}
    <script type="text/javascript" src="{{ ASSET_URL }}"></script>
{% endassets %}
'''
import models
import routes
import app_admin

app_admin.init_admin()

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(models.Maker).get(user_id)

    return login_manager

lm = init_login()


