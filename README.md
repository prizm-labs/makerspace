makerspace
==========

DIY web portal

#setup locla DB 
http://postgresapp.com/
http://inductionapp.com/
http://www.postgresguide.com/

sudo pip install pgsql

psql -h 127.0.0.1 -d makefoo

CREATE USER root WITH PASSWORD 'password';
CREATE DATABASE makefoo;
GRANT ALL PRIVILEGES ON DATABASE makefoo TO root;

COPY project (slug,title,description) FROM '/Users/mac/Documents/makerspace/table-project.csv' DELIMITERS ',' CSV;
COPY video (host_guid,project_id,name,path) FROM '/Users/mac/Documents/makerspace/table-video.csv' DELIMITERS ',' CSV;


Item > Component

Video > Chapter > Step

select pg_terminate_backend(pid) from pg_stat_activity where datname = 'makefoo';


python
>>from app import db
>>db.create_all()

cat ~/.ssh/id_rsa.pub | ssh root@makefoo.com "sudo sshcommand acl-add dokku MacMini2009"

ssh root@makefoo.com

if "pg_config executable not found."
install Command Line Tools
install Homebrew
brew install postgresql

sudo easy_install pip

pip install virtualenv
virtualenv .
. bin/activate

pip install -r requirements.txt


if Xcode 5.1 installed
"http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa"

sudo ARCHFLAGS="-arch x86_64" CFLAGS=-Wunused-command-line-argument-hard-error-in-future pip install psycopg2

git remote add prod dokku@makefoo.com:makefoo.com
git push prod master


gunicorn wsgi:app -b 0.0.0.0:7777 -w 3


8ae1ac34f82c2f62bba6b98ed668c67e
d395e429c4528343b2310a8070ad23bb
