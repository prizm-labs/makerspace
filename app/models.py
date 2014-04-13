from . import db

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

'''
related_projects = db.Table('related_projects',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)
'''


class Project(db.Model):
  #__tablename__ = "projects"

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(512))
  maker_id = db.Column(db.Integer, db.ForeignKey('maker.id'))

  tags = db.relationship('Tag', secondary=tags, backref=db.backref('project', lazy='dynamic'))

  videos = db.relationship('Video', backref='project', lazy='dynamic')

  steps = db.relationship('Step', backref='project', lazy='dynamic')

  components = db.relationship('Component', backref='project', lazy='dynamic')

  resources = db.relationship('Resource', backref='project', lazy='dynamic')

  #completion_time
  #difficulty
  #related_projects = db.relationship('Project', secondary=related_projects, backref=db.backref('project', lazy='dynamic'))

class Video(db.Model):
  #hosted on youtube or wistia
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  chapters = db.relationship('Chapter', backref='project', lazy='dynamic')
  host_guid = db.Column(db.String(80), unique=True) #i.e. Youtube "NVedGeVPc30"
  #host_id = 

class Resource(db.Model):
  #downloadable image, pdf, schematic
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  path = db.Column(db.String(80), unique=True)
  #type_id = 


class Tag(db.Model):
  #__tablename__ = "tags"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)


class Maker(db.Model):
  #__tablename__ = "makers"

  id = db.Column(db.Integer, primary_key=True)
  youtube_channel_url = db.Column(db.String(512))
  facebook_url = db.Column(db.String(512))
  twitter_handle = db.Column(db.String(40))
  email = db.Column(db.String(40))
  name = db.Column(db.String(80), unique=True) #i.e. KipKay
  alias = db.Column(db.String(80), unique=True) #i.e. Kip K.
  description = db.Column(db.String(512))
  logo_url = db.Column(db.String(512))
  headshot_url = db.Column(db.String(512))


class Chapter(db.Model):
  #__tablename__ = "chapters"

  id = db.Column(db.Integer, primary_key=True)
  video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
  title = db.Column(db.String(80), unique=True)
  start_time = db.Column(db.Integer())
  duration = db.Column(db.Integer())
  order = db.Column(db.Integer)


class Step(db.Model):
  #__tablename__ = "steps"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  start_time = db.Column(db.Integer())
  description = db.Column(db.String(255))
  order = db.Column(db.Integer)

  chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))

  resources = db.relationship('Resource', backref='step', lazy='dynamic')

  components = db.relationship('Component', backref='step', lazy='dynamic')


class Component(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
  quantity = db.Column(db.Integer)
  note = db.Column(db.String(255)) #size/portion i.e. 4"x4",  
  required = db.Column(db.Boolean)

#Component Set for alternate components  


class Product(db.Model):
  #__tablename__ = "products"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  
  month = db.Column(db.Integer)
  price = db.Column(db.Float)
  shop_url = db.Column(db.String(512))


class Item(db.Model): 
  #non-consumable > tool
  #consumable > material / part

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  type_id = db.Column(db.Integer, db.ForeignKey('type.id'))

  products = db.relationship('Product', backref='item', lazy='dynamic') #optional

