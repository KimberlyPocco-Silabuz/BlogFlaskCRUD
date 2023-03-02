from flask import Flask
from .config import Config
from .db import db
from app.routes.routes import app_router


def create_app():
    app = Flask(__name__)
    # Vamos a darle parametros de configuracion
    app.config.from_object(Config)
    # Registrar sus módulos de Blueprint:
    app.register_blueprint(app_router)
    # Vamos a crear la instancia de la DB para las migraciones:
    db.init_app(app)
    return app


