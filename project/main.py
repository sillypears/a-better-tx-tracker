
from flask import (Blueprint, current_app, render_template, request, send_file, url_for,)
from . import database as db

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def index():
  return render_template("index.html", nav="index", entries=db.get_entries())