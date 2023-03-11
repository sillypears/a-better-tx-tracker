from flask import g
from datetime import datetime
import re, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from . import models

def connect_db(conf):
  engine = create_engine(conf['SQLALCHEMY_DATABASE_URI'])
  if not database_exists(engine.url): 
    create_database(engine.url)
    
  print(engine)
  return engine

def get_makers():
  return models.Maker.query.order_by(models.Maker.name).all()