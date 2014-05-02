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

Base = models.Base
engine = create_engine('postgresql://root:password@127.0.0.1/makefoo', echo=True)
Customer = models.Customer
Supplier = models.Supplier
Meta = models.Meta
'''
from app import Base, Customer, Supplier, Meta, db
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:password@127.0.0.1/makefoo', echo=True)


Base.metadata.create_all(engine)

Base.metadata.drop_all(engine)



session = db.create_scoped_session()

session = Session(engine)

db.session.add_all([
    Customer(
        name='customer 1',
        metas=[
            Meta(
              data={'foo':'bar'})
        ]
    ),
    Supplier(
        company_name='Ace Hammers',
        metas=[
            Meta(
              data={'foo':'bar'})
        ]
    )
])

db.session.commit()

for customer in db.session.query(Customer):
    for m in customer.metas:
        print(m.data)
        print(m.parent.name)
'''