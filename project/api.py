

from flask import (Blueprint, Flask, jsonify, make_response, redirect,
                   render_template, request, send_file, url_for,)
from flask_api import status



api = Blueprint('api', __name__, url_prefix="/api")