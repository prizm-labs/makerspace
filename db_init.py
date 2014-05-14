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
#app.config.from_object('config')
db = SQLAlchemy(app)

engine = create_engine('postgresql://admin:password@127.0.0.1/makefoo', echo=True)
models.Base.metadata.drop_all(engine)
models.Base.metadata.create_all(engine)