from flask import Flask, send_from_directory
from flask_cors import CORS
from urllib.parse import urlparse
import os

from .extentions import db, migrate

url = urlparse(os.environ.get('DATABASE_URL'))

def create_app():
    # Dumb work around because heroku forces "postgres" and sqlalchemy only knows "postgresql"
    # So we replace the first instance of it if we find it
    db_url = os.environ.get('DATABASE_URL')
    if os.environ.get('DATABASE_URL').split(':')[0] == "postgres": 
        db_url = os.environ.get('DATABASE_URL').replace('postgres', 'postgresql', 1)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    @app.before_first_request
    def check_db():
        print('checking db')
        
    @app.after_request
    def add_header(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Access-Control-Allow-Headers, Origin, X-Requested-With, Content-Type, Accept, Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'
        return response

    from .routes.utils import utils as utils_blueprint
    app.register_blueprint(utils_blueprint)

    from .routes.api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')
    return app

    