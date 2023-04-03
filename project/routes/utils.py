

from flask import (Blueprint)

from ..extentions import db

utils = Blueprint('utils', __name__, url_prefix="/utils")
                 
@utils.route("/", methods=["GET"])
def util_home():
  return {'msg': 'some utility functions'}