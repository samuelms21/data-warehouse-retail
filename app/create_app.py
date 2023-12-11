# create_app.py

from flask import Flask
from app.config import Config
from app.extensions import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register blueprints
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app
