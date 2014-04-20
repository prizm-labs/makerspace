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



# How to setup local DB

http://inductionapp.com/
http://www.postgresguide.com/

sudo pip install pgsql

psql -h 127.0.0.1

CREATE USER root WITH PASSWORD 'password';
CREATE DATABASE makefoo;
GRANT ALL PRIVILEGES ON DATABASE makefoo TO root;
\q

# How to seed DB

python
>>from app import db
>>db.create_all()


psql -h 127.0.0.1 -d makefoo
\d+

COPY project (slug,title,description) FROM 
'../db/table-project.csv' 
DELIMITERS ',' CSV;

COPY video (host_guid,project_id,name,path) FROM 
'../db/table-video.csv' 
DELIMITERS ',' CSV;

COPY tags (tag_id,project_id) FROM 
'../db/table-tags.csv' 
DELIMITERS ',' CSV;


# from iMac 27"

COPY project (slug,title,description) FROM 
'/Users/dodeca/makerspace/db/project.csv' 
DELIMITERS ',' CSV;

COPY video (host_guid,project_id,name,path) FROM 
'/Users/dodeca/makerspace/db/video.csv' 
DELIMITERS ',' CSV;

COPY tag (id,name) FROM 
'/Users/dodeca/makerspace/db/tag.csv' 
DELIMITERS ',' CSV;

COPY tags (tag_id,project_id) FROM 
'/Users/dodeca/makerspace/db/tags.csv' 
DELIMITERS ',' CSV;



# How to kill pg process

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
