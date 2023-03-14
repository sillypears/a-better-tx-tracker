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
    
  return engine

def get_sales():
  return models.Sale.query.order_by(models.Sale.name).all()

def get_makers():
  return models.Maker.query.order_by(models.Maker.name).all()

def get_vendors():
  return models.Vendor.query.order_by(models.Vendor.name).all()

def get_entries():
  return models.Entry.query.order_by(models.Entry.id).all()

def get_entry(id):
  return models.Entry.query.filter_by(id=id)