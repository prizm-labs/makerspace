#from . import db
from sqlalchemy.dialects.postgresql import HSTORE

from sqlalchemy import *
import datetime
#from sqlalchemy import create_engine, Integer, Column, String, ForeignKey, Table

from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import Session, relationship, backref


ROLE_USER = 0
ROLE_ADMIN = 1


class Base(object):
    """Base class which provides automated table name
    and surrogate primary key column.

    """
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    #id = Column(Integer, primary_key=True)
    # cannot let 'id' be inherited
    # https://www.mail-archive.com/sqlalchemy@googlegroups.com/msg32619.html

    created_on = Column(DateTime, default=datetime.datetime.now)
    updated_on = Column(DateTime, onupdate=datetime.datetime.now)
    #info = Column(MutableDict.as_mutable(HSTORE), default=Meta())

Base = declarative_base(cls=Base)

# http://docs.sqlalchemy.org/en/rel_0_9/core/metadata.html


class MetaAssociation(Base):
    id = Column(Integer, primary_key=True)
    """Associates a collection of Address objects
    with a particular parent.

    """
    __tablename__ = "meta_association"

    @classmethod
    def creator(cls, discriminator):
        """Provide a 'creator' function to use with
        the association proxy."""

        return lambda metas:MetaAssociation(
                                metas=metas,
                                discriminator=discriminator)

    discriminator = Column(String)
    """Refers to the type of parent."""

    @property
    def parent(self):
        """Return the parent object."""
        return getattr(self, "%s_parent" % self.discriminator)


class Meta(Base):
  id = Column(Integer, primary_key=True)
  data = Column(MutableDict.as_mutable(HSTORE))
  # http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#sqlalchemy.dialects.postgresql.HSTORE

  association_id = Column(Integer,
                        ForeignKey("meta_association.id")
                    )

  association = relationship(
                    "MetaAssociation",
                    backref="metas")
  parent = association_proxy("association", "parent")


class HasMeta(object):

    """HasMeta mixin, creates a relationship to
    the meta_association table for each parent.

    """
    @declared_attr
    def meta_association_id(cls):
        return Column(Integer,
                                ForeignKey("meta_association.id"))

    @declared_attr
    def meta_association(cls):
        discriminator = cls.__name__.lower()
        cls.metas = association_proxy(
                    "meta_association", "metas",
                    creator=MetaAssociation.creator(discriminator)
                )
        return relationship("MetaAssociation",
                    backref=backref("%s_parent" % discriminator,
                                        uselist=False))

tags = Table('tags',Base.metadata,
    Column('tag_id', Integer, ForeignKey('tag.id')),
    Column('project_id', Integer, ForeignKey('project.id'))
)

related_projects = Table('related_projects',Base.metadata,
    Column('project_id', Integer, ForeignKey('project.id')),
    Column('related_project_id', Integer, ForeignKey('project.id'))
)

class Page(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  slug = Column(String(80), unique=True)
  title = Column(String(80))
  html = Column(Text)


class Project(HasMeta,Base):
  #__tablename__ = "projects"
  id = Column(Integer, primary_key=True)

  title = Column(String(80), unique=True)
  description = Column(String(512))
  maker_id = Column(Integer, ForeignKey('maker.id'))
  slug = Column(String(80), unique=True)
  #difficulty = Column(Integer)

  #many-to-many
  tags = relationship('Tag', secondary=tags, backref=backref('project', lazy='dynamic')) 

  #one-to-many
  videos = relationship('Video', backref='project', lazy='dynamic') #video 1 of N

  steps = relationship('Step', backref='project', lazy='dynamic')

  components = relationship('Component', backref='project', lazy='dynamic')

  resources = relationship('Resource', backref='project', lazy='dynamic')

  # http://stackoverflow.com/questions/9547298/adding-data-to-related-table-with-sqlalchemy
  '''
  related_projects = relationship("Project",
                secondary=related_projects,
                backref='related_to',
                primaryjoin=id == related_projects.c.project_id,
                secondaryjoin=id == related_projects.c.related_project_id)
  '''
  # http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers-contacts-and-friends
  related_projects = relationship('Project', 
        secondary=related_projects,
        #backref = backref('related_projects', lazy = 'dynamic'), 
        backref='related_to',
        primaryjoin = (related_projects.c.project_id == id), 
        secondaryjoin = (related_projects.c.related_project_id == id), 
        lazy = 'dynamic')

  # http://stackoverflow.com/questions/19258471/sqlalchemy-orm-init-method-vs
  #def __init__(self):
  #    self.metas = [Meta(data={'page_views': '0'})]

  #completion_time
  #difficulty
  #related_projects = relationship('Project', secondary=related_projects, backref=backref('project', lazy='dynamic'))


class Tag(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  name = Column(String(80), unique=True)


class Video(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  #hosted on youtube or wistia
  project_id = Column(Integer, ForeignKey('project.id'))
  name = Column(String(80), unique=True)
  host_guid = Column(String(80), unique=True) #i.e. Youtube "NVedGeVPc30"
  path = Column(String(80), unique=True)
  #thumbnail_path = Column(String(512))
  #host_id = 

  chapters = relationship('Chapter', backref='project', lazy='dynamic')
  

class Resource(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  #downloadable image, pdf, schematic
  project_id = Column(Integer, ForeignKey('project.id'))
  step_id = Column(Integer, ForeignKey('step.id'))
  name = Column(String(80))
  path = Column(String(80), unique=True)
  #type_id = 


class Maker(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  youtube_channel_url = Column(String(512))
  facebook_url = Column(String(512))
  twitter_handle = Column(String(40))
  email = Column(String(40))
  name = Column(String(80), unique=True) #i.e. KipKay
  alias = Column(String(80), unique=True) #i.e. Kip K.
  description = Column(String(512))
  logo_url = Column(String(512))
  headshot_url = Column(String(512))

class User(HasMeta,Base):
  id = Column(Integer, primary_key = True)
  nickname = Column(String(64), unique = True)
  email = Column(String(120), unique = True)
  role = Column(SmallInteger, default = ROLE_USER)
  #posts = relationship('Post', backref = 'author', lazy = 'dynamic')

  def is_authenticated(self):
      return True

  def is_active(self):
      return True

  def is_anonymous(self):
      return False

  def get_id(self):
      return unicode(self.id)

  def __repr__(self):
      return '<User %r>' % (self.nickname)


class Chapter(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  video_id = Column(Integer, ForeignKey('video.id'))
  title = Column(String(80), unique=True)
  start_time = Column(Integer())
  duration = Column(Integer())
  order = Column(Integer)


class Step(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  title = Column(String(80), unique=True)
  start_time = Column(Integer())
  description = Column(String(255))
  order = Column(Integer)

  project_id = Column(Integer, ForeignKey('project.id'))
  chapter_id = Column(Integer, ForeignKey('chapter.id'))

  resources = relationship('Resource', backref='step', lazy='dynamic')

  components = relationship('Component', backref='step', lazy='dynamic')


class Component(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  step_id = Column(Integer, ForeignKey('step.id'))
  project_id = Column(Integer, ForeignKey('project.id'))
  item_id = Column(Integer, ForeignKey('item.id'))
  quantity = Column(Integer)
  note = Column(String(255)) #size/portion i.e. 4"x4",  
  required = Column(Boolean)
  #Component Set for alternate components  


class Product(HasMeta,Base):
  id = Column(Integer, primary_key=True)
  name = Column(String(80), unique=True)
  description = Column(String(255))

  item_id = Column(Integer, ForeignKey('item.id'))
  
  price = Column(Float)
  shop_url = Column(String(512))


class Item(HasMeta,Base):
  #non-consumable > tool
  #consumable > material / part
  id = Column(Integer, primary_key=True)
  name = Column(String(80), unique=True)
  description = Column(String(255))
  note = Column(String(255))
  #type_id = Column(Integer, ForeignKey('type.id'))

  products = relationship('Product', backref='item', lazy='dynamic') #optional


class Customer(HasMeta, Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Supplier(HasMeta, Base):
    id = Column(Integer, primary_key=True)
    company_name = Column(String)


'''
class Kit(Base):
  id = Column(Integer, primary_key=True)
  name = Column(String(80), unique=True)
  description = Column(String(255))
  month = Column(Integer)
  difficulty = Column(Integer)

  products = relationship('Product', backref='item', lazy='dynamic') #optional
'''
