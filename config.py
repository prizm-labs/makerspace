import os
basedir = os.path.abspath(os.path.dirname(__file__))

# DEVELOPMENT CONFIGURATION

SECRET_KEY = 'dev'

SQLALCHEMY_DATABASE_URI = 'postgresql://admin:password@127.0.0.1/makefoo'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

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

AWS_ACCESS_KEY_ID = 'AKIAICWZEE2B3X6RGTIA'
AWS_SECRET_ACCESS_KEY = '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'
S3_BUCKET_NAME = 'thekingofrandom'
S3_USE_HTTPS = True
# S3_CDN_DOMAIN = ''
# S3_HEADERS = {}

COMPRESS_MIN_SIZE = 500
COMPRESS_LEVEL = 6

USE_S3 = True
# DEBUG = True