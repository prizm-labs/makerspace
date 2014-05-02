from . import db
from sqlalchemy.dialects.postgresql import HSTORE


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

related_projects = db.Table('related_projects',
    db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
    db.Column('related_project_id', db.Integer, db.ForeignKey('project.id'))
)


class Project(db.Model):
  #__tablename__ = "projects"

  id = db.Column(db.Integer(), primary_key=True)
  title = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(512))
  maker_id = db.Column(db.Integer, db.ForeignKey('maker.id'))
  slug = db.Column(db.String(80), unique=True)
  #difficulty = db.Column(db.Integer)

  #many-to-many
  tags = db.relationship('Tag', secondary=tags, backref=db.backref('project', lazy='dynamic')) 

  #one-to-many
  videos = db.relationship('Video', backref='project', lazy='dynamic') #video 1 of N

  steps = db.relationship('Step', backref='project', lazy='dynamic')

  components = db.relationship('Component', backref='project', lazy='dynamic')

  resources = db.relationship('Resource', backref='project', lazy='dynamic')

  # http://stackoverflow.com/questions/9547298/adding-data-to-related-table-with-sqlalchemy
  related_projects = db.relationship("Project",
                secondary=related_projects,
                backref='related_to',
                primaryjoin=id == related_projects.c.project_id,
                secondaryjoin=id == related_projects.c.related_project_id)

  #meta = db.relationship('Meta', backref='project', lazy='dynamic')

  #completion_time
  #difficulty
  #related_projects = db.relationship('Project', secondary=related_projects, backref=db.backref('project', lazy='dynamic'))

class Tag(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)

'''
class Meta(db.Model):

  id  = db.Column(db.Integer, primary_key=True)
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  data = db.Column(HSTORE)
  # http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#sqlalchemy.dialects.postgresql.HSTORE
'''

class Video(db.Model):
  #hosted on youtube or wistia
  id = db.Column(db.Integer, primary_key=True)
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  name = db.Column(db.String(80), unique=True)
  host_guid = db.Column(db.String(80), unique=True) #i.e. Youtube "NVedGeVPc30"
  path = db.Column(db.String(80), unique=True)
  #thumbnail_path = db.Column(db.String(512))
  #host_id = 

  chapters = db.relationship('Chapter', backref='project', lazy='dynamic')
  

class Resource(db.Model):
  #downloadable image, pdf, schematic
  id = db.Column(db.Integer, primary_key=True)
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  step_id = db.Column(db.Integer, db.ForeignKey('step.id'))
  name = db.Column(db.String(80))
  path = db.Column(db.String(80), unique=True)
  #type_id = 


class Maker(db.Model):

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

  id = db.Column(db.Integer, primary_key=True)
  video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
  title = db.Column(db.String(80), unique=True)
  start_time = db.Column(db.Integer())
  duration = db.Column(db.Integer())
  order = db.Column(db.Integer)


class Step(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True)
  start_time = db.Column(db.Integer())
  description = db.Column(db.String(255))
  order = db.Column(db.Integer)

  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))

  resources = db.relationship('Resource', backref='step', lazy='dynamic')

  components = db.relationship('Component', backref='step', lazy='dynamic')


class Component(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  step_id = db.Column(db.Integer, db.ForeignKey('step.id'))
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
  item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
  quantity = db.Column(db.Integer)
  note = db.Column(db.String(255)) #size/portion i.e. 4"x4",  
  required = db.Column(db.Boolean)
  #Component Set for alternate components  


class Product(db.Model):

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))

  item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
  
  price = db.Column(db.Float)
  shop_url = db.Column(db.String(512))


class Item(db.Model):
  #non-consumable > tool
  #consumable > material / part

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  note = db.Column(db.String(255))
  #type_id = db.Column(db.Integer, db.ForeignKey('type.id'))

  products = db.relationship('Product', backref='item', lazy='dynamic') #optional

"""discriminator_on_related.py

The HasAddresses mixin will provide a relationship
to the fixed Address table based on a fixed association table.

The association table will also contain a "discriminator"
which determines what type of parent object associates to the
Address row.

This is a "polymorphic association".   Even though a "discriminator"
that refers to a particular table is present, the extra association
table is used so that traditional foreign key constraints may be used.

This configuration has the advantage that a fixed set of tables
are used, with no extra-table-per-parent needed.   The individual
Address record can also locate its parent with no need to scan
amongst many tables.

"""

from sqlalchemy import create_engine, Integer, Column, String, ForeignKey, Table

from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.associationproxy import association_proxy

from sqlalchemy.orm import Session, relationship, backref



class Base(object):
    """Base class which provides automated table name
    and surrogate primary key column.

    """
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    id = db.Column(db.Integer, primary_key=True)
Base = declarative_base(cls=Base)


class MetaAssociation(Base):
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

    discriminator = db.Column(db.String)
    """Refers to the type of parent."""

    @property
    def parent(self):
        """Return the parent object."""
        return getattr(self, "%s_parent" % self.discriminator)


class Meta(Base):

  id  = db.Column(db.Integer, primary_key=True)
  data = db.Column(MutableDict.as_mutable(HSTORE))
  # http://docs.sqlalchemy.org/en/rel_0_9/dialects/postgresql.html#sqlalchemy.dialects.postgresql.HSTORE

  association_id = db.Column(db.Integer,
                        db.ForeignKey("meta_association.id")
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
        return db.Column(db.Integer,
                                db.ForeignKey("meta_association.id"))

    @declared_attr
    def meta_association(cls):
        discriminator = cls.__name__.lower()
        cls.metas = association_proxy(
                    "meta_association", "metas",
                    creator=MetaAssociation.creator(discriminator)
                )
        return db.relationship("MetaAssociation",
                    backref=backref("%s_parent" % discriminator,
                                        uselist=False))
'''
class Address(Base):
    """The Address class.

    This represents all address records in a
    single table.

    """
    association_id = Column(Integer,
                        ForeignKey("address_association.id")
                    )
    street = Column(String)
    city = Column(String)
    zip = Column(String)
    association = relationship(
                    "AddressAssociation",
                    backref="addresses")

    parent = association_proxy("association", "parent")

    def __repr__(self):
        return "%s(street=%r, city=%r, zip=%r)" % \
            (self.__class__.__name__, self.street,
            self.city, self.zip)


class HasAddresses(object):
    """HasAddresses mixin, creates a relationship to
    the address_association table for each parent.

    """
    @declared_attr
    def address_association_id(cls):
        return Column(Integer,
                                ForeignKey("address_association.id"))

    @declared_attr
    def address_association(cls):
        discriminator = cls.__name__.lower()
        cls.addresses= association_proxy(
                    "address_association", "addresses",
                    creator=AddressAssociation.creator(discriminator)
                )
        return relationship("AddressAssociation",
                    backref=backref("%s_parent" % discriminator,
                                        uselist=False))
'''

class Customer(HasMeta, Base):
    name = Column(String)

class Supplier(HasMeta, Base):
    company_name = Column(String)



'''
class Kit(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))
  month = db.Column(db.Integer)
  difficulty = db.Column(db.Integer)

  products = db.relationship('Product', backref='item', lazy='dynamic') #optional
'''
