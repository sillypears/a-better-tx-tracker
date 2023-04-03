from flask import g
from datetime import datetime

from .models.entry import Entry
from .models.sale import Sale
from .models.maker import Maker
from .models.vendor import Vendor
from .extentions import db

# Get requests
def get_paged_ids(id: int):
  control = {"results": {"prev": -1, "next": -1}} 
  prev_item = Entry.query.order_by(Entry.purchase_date.desc()).filter(Entry.id < id).first()
  next_item = Entry.query.order_by(Entry.purchase_date.asc()).filter(Entry.id > id).first()
  print(next_item)
  if prev_item is not None and prev_item.id > 0: control["results"]["prev"] = prev_item.id
  if next_item is not None and next_item.id > 0: control["results"]["next"] = next_item.id
  return control
  
def get_sales() -> list[Sale]:
  return Sale.query.order_by(Sale.name).all()

def get_makers() -> list[Maker]:
  return Maker.query.order_by(Maker.name).all()

def get_vendors() -> list[Vendor]:
  return Vendor.query.order_by(Vendor.name).all()

def get_entries() -> list[Entry]:
  return Entry.query.order_by(Entry.purchase_date.desc()).all()

def get_entries_paginated(limit, offset) -> list[Entry]:
  print(offset, limit)
  return Entry.query.order_by(Entry.purchase_date.desc()).offset(offset).limit(limit).all()

def get_entries_total() -> int:
  return Entry.query.count()

def get_entry(needle_id: int) -> Entry:
  return Entry.query.filter_by(id=needle_id).one()

# Update requests
def toggle_received_status(needle_id: int, conf=object) -> Entry:

  status = Entry.query.filter_by(id=needle_id).one()
  status.received = False if status.received == True else True
  db.session.commit()
  return status

def update_entry(needle_id: int, entry_data) -> Entry:
  entry = Entry
  try:
    entry = Entry.query.filter_by(id=needle_id).one()
    entry
  except:
    pass
  return entry