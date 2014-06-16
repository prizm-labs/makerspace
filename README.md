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

pip freeze > requirements.txt



# How to setup local DB

http://inductionapp.com/
http://www.postgresguide.com/

sudo pip install pgsql

psql -h 127.0.0.1


CREATE USER admin WITH PASSWORD 'password';
CREATE DATABASE makefoo;
GRANT ALL PRIVILEGES ON DATABASE makefoo TO admin;
\q

# Install HSTORE extension
# http://www.postgresql.org/docs/9.1/static/sql-createextension.html
psql -h 127.0.0.1 -d makefoo
create extension hstore;
\d+;


# clear and reset database

# How to kill pg process
# http://blog.gahooa.com/2010/11/03/how-to-force-drop-a-postgresql-database-by-killing-off-connection-processes/
ps -a

psql -h 127.0.0.1
select pg_terminate_backend(pid) from pg_stat_activity where datname = 'makefoo';


DROP DATABASE makefoo;
CREATE DATABASE makefoo;
GRANT ALL PRIVILEGES ON DATABASE makefoo TO root;
\q

psql -h 127.0.0.1 -d makefoo
create extension hstore;
\q 

\d+;


# How to seed DB

# Create tables

python >>
from app import Base, engine

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# Populate tables

python db_init.py
python db_seed.py



# add default meta to all projects

python >>
from app import models, db

projects = db.session.query(models.Project).all()

for p in projects:
  p.metas = [Meta(data={'page_views': '0'})]

db.session.commit()




# How to setup production DB


# dump local DB
# http://www.postgresql.org/docs/9.1/static/backup-dump.html

# http://stackoverflow.com/questions/3274397/reload-profile-in-bash-shell-script-in-unix
source ~/.profile
source ~/.bashrc

pg_dump -h 127.0.0.1 makefoo > dump.txt --no-owner --no-privileges


https://github.com/jeffutter/dokku-postgresql-plugin
https://github.com/Kloadut/dokku-pg-plugin







# How to setup deployment

# deploy with Dokku

cat ~/.ssh/id_rsa.pub | ssh root@makefoo.com "sudo sshcommand acl-add dokku MacMini2009"

ssh root@makefoo.com

git remote add prod dokku@makefoo.com:makefoo.com
git push prod master


# deploy on Ubuntu

sudo apt-get install libapache2-mod-wsgi 
sudo a2enmod wsgi 
apt-get update
sudo apt-get install python-pip 

cd /var/www/makerspace
sudo virtualenv venv
sudo pip install Flask 

# https://www.digitalocean.com/community/articles/how-to-install-and-use-postgresql-on-ubuntu-12-04
sudo apt-get install postgresql postgresql-contrib


# https://jordanktakayama.wordpress.com/2013/02/20/lessons-learned-from-deploying-django-on-heroku/

# https://help.ubuntu.com/community/PostgreSQL
sudo -u postgres psql postgres
sudo -u postgres createuser --superuser admin

sudo -u postgres psql
=# \password admin

apt-get install -y libxml2-dev libxslt1-dev
apt-get install -y nginx uwsgi uwsgi-plugin-python

sudo apt-get install python-dev
sudo apt-get install python-psycopg2
sudo apt-get install libpq-devpip 

psql
# create 'makefoo' DB and install hstore extension
CREATE USER admin WITH PASSWORD 'password';
CREATE DATABASE makefoo;
GRANT ALL PRIVILEGES ON DATABASE makefoo TO admin;
grant all on all tables in schema public to admin;
\q

# Install HSTORE extension
# http://www.postgresql.org/docs/9.1/static/sql-createextension.html
psql -h 127.0.0.1 -d makefoo
create extension hstore;
\d+;


psql makefoo < dump.txt


source venv/bin/activate 

pip install -r requirements.txt


cd /var/www/makerspace
source venv/bin/activate 


# How to run app locally
source venv/bin/activate 
python wsgi.py

gunicorn wsgi:app -b 0.0.0.0:7777 -w 3

# Production Server

ssh root@107.170.146.204
rzpmnoaogmoj


8ae1ac34f82c2f62bba6b98ed668c67e
d395e429c4528343b2310a8070ad23bb
