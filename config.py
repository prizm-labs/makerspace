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
