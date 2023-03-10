

from flask import (Blueprint, Flask, jsonify, make_response, redirect,
                   render_template, request, send_file, url_for,)
from flask_api import status



main = Blueprint('main', __name__)