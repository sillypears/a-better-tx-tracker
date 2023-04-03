
from flask import (Blueprint, current_app, render_template, send_from_directory,) 
from .. import database as db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def index():
  rowcount = current_app.config['ROWNUM']
  
  return render_template("index.html", nav="index", entries=db.get_entries_paginated(0,rowcount*2), total_entries=db.get_entries_total())

@main.route("/entry", methods=["GET"])
def entry():
  return render_template("entry.html", nav="entry", entry=None)

@main.route("/entry/<id>", methods=["GET"])
def entry_id(id):
  entry = db.get_entry(id)
  return render_template("entry.html", nav="entry", entry=entry, control=db.get_paged_ids(id))
