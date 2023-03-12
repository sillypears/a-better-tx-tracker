

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
