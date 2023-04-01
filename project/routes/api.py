

from flask import (Blueprint, current_app, Flask, jsonify, make_response, redirect,
                   render_template, request, send_file, url_for,)
import json
from sqlalchemy.schema import CreateSchema
from .. import database

api = Blueprint('api', __name__, url_prefix="/api")

@api.route("/", methods=["GET"])
def api_index():
  conf = current_app.config
  return { "version": f"{conf['MAJOR_VERSION']}.{conf['MINOR_VERSION']}" }

@api.route('/makers', methods=["GET", "POST"])
def api_makers():
  if request.method == "GET":
    return jsonify(database.get_makers())
  
  if request.method == "POST":
    pass
  
@api.route('/vendors', methods=["GET", "POST"])
def get_vendors():
  if request.method == "GET":
    return jsonify(database.get_vendors())
  
  if request.method == "POST":
    pass

@api.route('/sales', methods=["GET", "POST"])
def api_sales():
  if request.method == "GET":
    return jsonify(database.get_sales())
  
  if request.method == "POST":
    pass
  
@api.route('/entries', methods=["GET", "POST"])
def api_entries():
  if request.method == "GET":
    return jsonify(database.get_entries())
  
  if request.method == "POST":
    pass

@api.route('/entries/<offset>', defaults={'limit':None}, methods=["GET", "POST"])
@api.route('/entries/<offset>/<limit>', methods=["GET", "POST"])

def api_entries_paginated(offset, limit):
  if limit is None: int(offset),current_app.config['ROWNUM']
  
  if request.method == "GET":
    return jsonify(database.get_entries_paginated(int(offset), int(limit)))
  
  if request.method == "POST":
    pass

@api.route('/entry', methods=["GET"])
def api_entry_base():
  return jsonify({"pick": "an entry"})

@api.route('/entry/<id>', methods=["GET"])
def api_entry(id):
  try:
    print(id)
    entry = database.get_entry(id)
  except Exception as e:
    entry = {"nope": "found nothing", "err": str(e)}
  return jsonify(entry)

@api.route('/toggleEntry', methods=["GET", "POST"])
def api_toggle_entries():
  if request.method == "GET":
    try:
      entry = int(request.args.to_dict()['id'])
      result = database.toggle_received_status(entry)
    except:
      result = f"but I couldn't find {request.args.to_dict()}"
    return jsonify(f"got it {result}")
  try:
    entry = json.loads(request.data.decode('utf-8'))['toggleId']
    result = database.toggle_received_status(entry)
  except Exception as e:
    print(e)
  return jsonify({'status': 'ok'})

@api.route('/totalEntries', methods=["GET"])
def api_total_entries():
  return jsonify({'total_entries': len(database.get_entries())})