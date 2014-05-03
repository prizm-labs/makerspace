makerspace
==========

DIY web portal




# How to setup Python environment

sudo easy_install pip

sudo pip install virtualenv
virtualenv .
. bin/activate

- Install Posgres 
http://postgresapp.com/

- if "pg_config executable not found."
install Command Line Tools
install Homebrew
brew install postgresql -verbose

which pg_config

- if Xcode 5.1 installed
"http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa"

sudo ARCHFLAGS="-arch x86_64" CFLAGS=-Wunused-command-line-argument-hard-error-in-future pip install psycopg2

pip install -r requirements.txt

virtualenv venv
source venv/bin/activate
deactivate

pip freeze requirements.txt



# How to setup local DB

http://inductionapp.com/
http://www.postgresguide.com/

sudo pip install pgsql

psql -h 127.0.0.1


CREATE USER root WITH PASSWORD 'password';
CREATE DATABASE makefoo;
GRANT ALL PRIVILEGES ON DATABASE makefoo TO root;
USE makefoo;
create extension hstore;

\q

DROP DATABASE makefoo;


# How to seed DB

# Install HSTORE extension
# http://www.postgresql.org/docs/9.1/static/sql-createextension.html
psql -h 127.0.0.1 -d makefoo
create extension hstore;
\d+;




# Create tables

python >>
from app import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Populate tables

python import.py



# add default meta to all projects

python >>
from app import models, db

projects = db.session.query(models.Project).all()

for p in projects:
  p.metas = [Meta(data={'page_views': '0'})]

db.session.commit()




# How to setup production DB

https://github.com/jeffutter/dokku-postgresql-plugin
https://github.com/Kloadut/dokku-pg-plugin



# How to kill pg process
# http://blog.gahooa.com/2010/11/03/how-to-force-drop-a-postgresql-database-by-killing-off-connection-processes/
ps -a

psql -h 127.0.0.1
select pg_terminate_backend(pid) from pg_stat_activity where datname = 'makefoo';





# How to setup deployment

cat ~/.ssh/id_rsa.pub | ssh root@makefoo.com "sudo sshcommand acl-add dokku MacMini2009"

ssh root@makefoo.com

git remote add prod dokku@makefoo.com:makefoo.com
git push prod master




# How to run app locally

python wsgi.py

gunicorn wsgi:app -b 0.0.0.0:7777 -w 3




8ae1ac34f82c2f62bba6b98ed668c67e
d395e429c4528343b2310a8070ad23bb
