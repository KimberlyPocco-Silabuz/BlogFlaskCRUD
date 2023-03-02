from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

from app.routes.app import app_router
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(app_router) 
    db= SQLAlchemy(app)
    return app