# http://flask-script.readthedocs.org/en/latest/

# http://blog.miguelgrinberg.com/post/flask-migrate-alembic-database-migration-wrapper-for-flask

# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

from app import app, db

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()