import csv
from app import db,models
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


engine = create_engine('postgresql://root:password@127.0.0.1/makefoo', echo=True)
models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)


# from iMac 27"
# from Mac Mini
root_dir = '/Users/dodeca/makerspace/db/'

def create_project(columns):
  row = models.Project(slug=columns[0],title=columns[1],description=columns[2],metas=[models.Meta(data={'page_views': '0'})])
  return row

def create_video(columns):
  row = models.Video(host_guid=columns[0],project_id=columns[1],name=columns[2],path=columns[3])
  return row

def create_tag(columns):
  row = models.Tag(id=columns[0],name=columns[1])
  return row

table_creators = {'project':create_project, 'video':create_video, 'tag':create_tag}

def import_model(table_name):
  with open(root_dir+table_name+'.csv', 'Ur') as f:
    data = list(tuple(rec) for rec in csv.reader(f, delimiter=','))
    rows = []
    for row in data:
      print row
      creator = table_creators[table_name]
      rows.append(creator(row))
    db.session.add_all(rows)
    db.session.commit()

def import_all_models():
  models_to_import = ['project','video','tag']

  for m in models_to_import:
    import_model(m)


import_all_models()

#TODO create association tables
'''
psql -h 127.0.0.1 -d makefoo

COPY tags (tag_id,project_id) FROM 
'/Users/dodeca/makerspace/db/tags.csv' 
DELIMITERS ',' CSV;

COPY related_projects (project_id,related_project_id) FROM 
'/Users/dodeca/makerspace/db/related_projects.csv' 
DELIMITERS ',' CSV;
'''



'''
psql -h 127.0.0.1 -d makefoo

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