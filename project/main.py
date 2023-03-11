
from flask import (Blueprint, Flask, jsonify, make_response, redirect,
                   render_template, request, send_file, url_for,)
from . import database as db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def index():
  return render_template("index.html", nav="index", s=db.get_makers())