import os
basedir = os.path.abspath(os.path.dirname(__file__))

# DEVELOPMENT CONFIGURATION

SECRET_KEY = 'dev'

SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@127.0.0.1/makefoo'

# flag for packaging static assets
ASSETS_DEBUG = True

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'michael.a.garrido'
MAIL_PASSWORD = 'fOOlyc00!!y'
# administrator list
ADMINS = ['michael.a.garrido@gmail.com']

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
