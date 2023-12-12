# create_app.py

from flask import Flask
from app.config import Config
from app.extensions import db
from app.generate_dummy_data import generate_dummy_data


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()
        generate_dummy_data(db)

    # Register blueprints
    from app.routes.store_routes import store_bp
    app.register_blueprint(store_bp)

    return app
