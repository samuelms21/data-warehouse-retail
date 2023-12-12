# run.py

from app import create_app
from app.commands.generate_dummy_data import generate_dummy_data
from app.extensions import db

app = create_app()

with app.app_context():
    generate_dummy_data()

if __name__ == "__main__":
    app.run()