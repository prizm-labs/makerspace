import csv
from app import db,models
from sqlalchemy.orm import Session
from sqlalchemy import func

projects_to_feature = [1,5,10,12]
featured_tag_id = 55

projects = db.session.query(models.Project).filter(models.Project.id.in_(projects_to_feature)).all()

# get 'featured' tag
featured_tag = db.session.query(models.Tag).filter(models.Tag.id==featured_tag_id).first()
print featured_tag

for p in projects: 
  print '---'
  print len(p.tags)

    # test if already tagged 'featured'
    # http://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value

  #if (any(func.lower(t.name) == "featured" for t in p.tags)):
  if (any(t.id == featured_tag_id for t in p.tags)):
    print 'already featured'
  else:
    print 'not featured'

    p.tags.append(featured_tag)

    for t in p.tags:
      print t.name
    
    

  

db.session.commit()

  

