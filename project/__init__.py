from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from urllib.parse import urlparse
import os

from . import database

# init SQLAlchemy so we can use it later in our models
db = None

url = urlparse(os.environ.get('DATABASE_URL'))

class Config(object):
    DEBUG = True if os.environ.get('FLASK_ENV') == "development" else False
    DATABASE_HOST = url.hostname
    DATABASE_PORT = url.port
    DATABASE_USER = url.username
    DATABASE_PASS = url.password
    DATABASE_SCHEMA = url.path[1:]

def create_app():
    # Dumb work around because heroku forces "postgres" and sqlalchemy only knows "postgresql"
    # So we replace the first instance of it if we find it
    db_url = os.environ.get('DATABASE_URL')
    if os.environ.get('DATABASE_URL').split(':')[0] == "postgres": 
        db_url = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql', 1)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['CONFIG'] = Config   
    app.config['majorVersion'] = 1
    app.config['minorVersion'] = 0.1
    CORS(app)
    db = SQLAlchemy(app)
    with app.app_context():
      db.create_all()
      db.session.commit()
    # db.init_app(app)
    print(vars(db))
    
    # from . import models
    # database.connect_db(app.config)
                              
    @app.after_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
        return response
        
    # blueprint for auth routes in our app

    # from .utils import utils as utils_blueprint
    # app.register_blueprint(utils_blueprint)

    # from .api import api as api_blueprint
    # app.register_blueprint(api_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

    