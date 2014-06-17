import csv
from flask import Flask
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask.ext.sqlalchemy import SQLAlchemy

#from app import db,models
import sys
sys.path.append("app/")
import models

app = Flask(__name__,static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


# from iMac 27"
# from Mac Mini
root_dir = '/Users/dodeca/makerspace/db/'

def create_project(columns):
  row = models.Project(id=columns[0],created_on=columns[1],slug=columns[2],title=columns[3],description=columns[4],full_description=columns[5],metas=[models.Meta(data={'page_views': '0'})])
  return row

def create_video(columns):
  row = models.Video(project_id=columns[0],posted_on=columns[1],host_guid=columns[2],name=columns[3],path=columns[4])
  return row

def create_tag(columns):
  row = models.Tag(id=columns[0],name=columns[1])
  return row

def create_page(columns):
  row = models.Page(slug=columns[0],title=columns[1],html=columns[2])
  return row

table_creators = {'project':create_project, 'video':create_video, 'tag':create_tag, 'page': create_page}

def import_model(table_name):
  with open(root_dir+table_name+'.csv', 'Ur') as f:
    data = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
    rows = []
    for row in data:
      #print row
      creator = table_creators[table_name]
      rows.append(creator(row))
    db.session.add_all(rows)
    db.session.commit()

def import_all_models():
  models_to_import = ['project','video','tag','page']

  for m in models_to_import:
    import_model(m)


import_all_models()

#TODO create association tables
'''
psql -h 127.0.0.1 -d makefoo

INSERT INTO maker (nickname,email,role) VALUES ('michael.a.garrido','michael.a.garrido@gmail.com',1);                                               ;

COPY tags (tag_id,project_id) FROM 
'/Users/dodeca/makerspace/db/tags.csv' 
DELIMITERS ',' CSV;

COPY related_projects (project_id,related_project_id) FROM 
'/Users/dodeca/makerspace/db/related_projects.csv' 
DELIMITERS ',' CSV;
'''



'''
psql -h 127.0.0.1 -d makefoo

COPY page (slug,title,html) FROM 
'/Users/dodeca/makerspace/db/page.csv' 
DELIMITERS ',' CSV;

COPY project (slug,title,description) FROM 
'/Users/dodeca/makerspace/db/project.csv' 
DELIMITERS ',' CSV;

COPY video (host_guid,project_id,name,path) FROM 
'/Users/dodeca/makerspace/db/video.csv' 
DELIMITERS ',' CSV;

COPY tag (id,name) FROM 
'/Users/dodeca/makerspace/db/tag.csv' 
DELIMITERS ',' CSV;
'''



'''
from app import Base, Customer, Supplier, Meta, db, engine
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


Base.metadata.create_all(engine)

Base.metadata.drop_all(engine)
'''