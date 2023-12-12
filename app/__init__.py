# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .extensions import db
from .routes.store_routes import store_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db = SQLAlchemy(app)

    db.init_app(app)

    from .models import store_model

    with app.app_context():
        db.create_all()

    app.register_blueprint(store_bp)

    return app