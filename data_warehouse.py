import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import Transaction, DateModel, Product, Store

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'Transaction': Transaction, 'DateModel': DateModel, 'Product': Product, 'Store': Store}