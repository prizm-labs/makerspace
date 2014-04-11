from . import db


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)


related_projects = db.Table('related_projects',
    db.Column('projectA_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('projectB_id', db.Integer, db.ForeignKey('project.id'))
)


class Project(db.Model):
  __tablename__ = "projects"

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  youtube_url = db.Column(db.String(512))
  download_url = db.Column(db.String(512))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
  maker_id = db.Column(db.Integer, db.ForeignKey('maker.id'))

  tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('project', lazy='dynamic'))

  chapters = db.relationship('Chapter', backref='project',
                                lazy='dynamic')

  products = db.relationship('Product', backref='project',
                                lazy='dynamic')

  #completion_time
  #difficulty

  related_projects = db.relationship('Project', secondary=related_projects,
        backref=db.backref('project', lazy='dynamic'))


class Tag(db.Model):
  __tablename__ = "tags"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)


class Maker(db.Model):
   __tablename__ = "makers"

  id = db.Column(db.Integer, primary_key=True)
  youtube_channel_url = db.Column(db.String(512))
  facebook_url = db.Column(db.String(512))
  twitter_handle = db.Column(db.String(40))
  email = db.Column(db.String(40))
  name = db.Column(db.String(80), unique=True)
  alias = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(512))
  logo_url = db.Column(db.String(512))
  headshot_url = db.Column(db.String(512))


class Product(db.Model):
  __tablename__ = "products"

  id = db.Column(db.Integer, primary_key=True)
  month = db.Column(db.Integer)
  price = db.Column(db.Float)
  difficulty = db.Column(db.Integer)
  shop_url = db.Column(db.String(512))



class Chapter(db.Model):
  __tablename__ = "chapters"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  start_time = db.Column(db.Integer())
  #end_time = db.Column(db.Integer())
  order = db.Column(db.Integer)
  steps = db.relationship('Step', backref='chapter',
                                lazy='dynamic')


class Step(db.Model):
  __tablename__ = "steps"

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  start_time = db.Column(db.Integer())
  description = db.Column(db.String(255))
  order = db.Column(db.Integer)


class Tool(db.Model): #non-consumable
  __tablename__ = "tools"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  price = db.Column(db.Float)


class Material(db.Model): #consumable
  __tablename__ = "materials"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  price = db.Column(db.Float)