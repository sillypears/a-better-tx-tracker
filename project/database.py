from flask import g
from datetime import datetime
import re, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from . import models

def connect_db(conf: object):
  engine = create_engine(conf['SQLALCHEMY_DATABASE_URI'])
  if not database_exists(engine.url): 
    create_database(engine.url)
    
  return engine

def get_next_id(id: int):
  control = {"results": {"prev": -1, "next": -1}} 
  prev_item = models.Entry.query.order_by(models.Entry.purchase_date.desc()).filter(models.Entry.id < id).first()
  next_item = models.Entry.query.order_by(models.Entry.purchase_date.asc()).filter(models.Entry.id > id).first()
  print(next_item)
  if prev_item is not None and prev_item.id > 0: control["results"]["prev"] = prev_item.id
  if next_item is not None and next_item.id > 0: control["results"]["next"] = next_item.id
  return control
  
def get_sales():
  return models.Sale.query.order_by(models.Sale.name).all()

def get_makers():
  return models.Maker.query.order_by(models.Maker.name).all()

def get_vendors():
  return models.Vendor.query.order_by(models.Vendor.name).all()

def get_entries():
  return models.Entry.query.order_by(models.Entry.purchase_date.desc()).all()

def get_entries_paginated(limit, offset):
  print(offset, limit)
  return models.Entry.query.order_by(models.Entry.purchase_date.desc()).offset(offset).limit(limit).all()

def get_entries_total():
  return models.Entry.query.count()

def get_entry(id: int):
  return models.Entry.query.filter_by(id=id)