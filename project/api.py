

from flask import (Blueprint, current_app, Flask, jsonify, make_response, redirect,
                   render_template, request, send_file, url_for,)
from sqlalchemy.schema import CreateSchema
# from flask_api import status
from . import database as db
from . import models


api = Blueprint('api', __name__, url_prefix="/api")




@api.route("/", methods=["GET"])
def api_index():
  conf = current_app.config
  return { "version": f"{conf['MAJOR_VERSION']}.{conf['MINOR_VERSION']}" }

@api.route('/makers', methods=["GET", "POST"])
def api_makers():
  if request.method == "GET":
    return jsonify(db.get_makers())
  
  if request.method == "POST":
    pass
  
@api.route('/vendors', methods=["GET", "POST"])
def get_vendors():
  if request.method == "GET":
    return jsonify(db.get_vendors())
  
  if request.method == "POST":
    pass

@api.route('/sales', methods=["GET", "POST"])
def api_sales():
  if request.method == "GET":
    return jsonify(db.get_sales())
  
  if request.method == "POST":
    pass
  
@api.route('/entries', methods=["GET", "POST"])
def api_entries():
  if request.method == "GET":
    return jsonify(db.get_entries())
  
  if request.method == "POST":
    pass

@api.route('/entries/<offset>', defaults={'limit':None}, methods=["GET", "POST"])
@api.route('/entries/<offset>/<limit>', methods=["GET", "POST"])

def api_entries_paginated(offset, limit):
  if limit is None: int(offset),current_app.config['ROWNUM']
  
  if request.method == "GET":
    return jsonify(db.get_entries_paginated(int(offset), int(limit)))
  
  if request.method == "POST":
    pass

@api.route('/totalEntries', methods=["GET"])
def api_total_entries():
  return jsonify({'total_entries': len(db.get_entries())})