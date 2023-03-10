from flask import g
import psycopg2
from datetime import datetime
import re, json
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def connect_db(conf):
  engine = create_engine(conf['SQLALCHEMY_DATABASE_URI'])
  if not database_exists(engine.url): 
    create_database(engine.url)
    
  print(engine)
  return engine

# def get_db(conf):
#     db = psycopg2.connect(
#         user = conf.DATABASE_USER,
#         password = conf.DATABASE_PASS,
#         database = conf.DATABASE_SCHEMA,
#         port = conf.DATABASE_PORT,
#         host= conf.DATABASE_HOST,        
#         )
#     db.autocommit = True
#     return db

def close_db(db, conf):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

def get_makers(db, user_id, conf):
  cur = db.cursor()
  cur.execute(f"SELECT id, name, display, instagram FROM makers WHERE user_id = {user_id} ORDER BY name ASC")
    