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

from flask.ext.assets import Environment, Bundle

from flask.ext.admin import Admin
from flask.ext.login import LoginManager

from flask.ext.babel import Babel
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:password@127.0.0.1/makefoo'
app.config['ASSETS_DEBUG'] = True

db = SQLAlchemy(app)
babel = Babel(app)

login_manager = LoginManager()
login_manager.init_app(app)

# http://flask-assets.readthedocs.org/en/latest/
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

from admin_views import *

admin = Admin(app)
add_admin_views(admin)
# Add administrative views here