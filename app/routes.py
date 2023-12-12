from app import app, db
from flask import jsonify, request
import sqlalchemy as sa
from app.models import Product, Store, DateModel, Transaction

# Function index() will run when request is made to "/" or "/index"
@app.route("/")
@app.route("/index")
def index():
    return "Hello World"


# Retrieve all products
@app.route("/products", methods=["GET"])
def get_products():
    query = sa.select(Product)
    all_products = db.session.scalars(query).all()

    serialized_products = []

    for product in all_products:
        item = {
            "id": product.id,
            "name": product.name,
            "brand": product.brand,
            "category": product.category,
            "department": product.department,
        }
        serialized_products.append(item)

    return jsonify(serialized_products)


# Retrieve all stores
@app.route("/stores", methods=["GET"])
def get_stores():
    query = sa.select(Store)
    all_stores = db.session.scalars(query).all()

    serialized_stores = []

    for store in all_stores:
        item = {
            "id": store.id,
            "name": store.name,
            "address": store.address,
            "phone": store.phone
        }
        serialized_stores.append(item)

    return jsonify(serialized_stores)


# Retrieve all dates instances
@app.route("/dates", methods=["GET"])
def get_dates():
    query = sa.select(DateModel)
    all_dates = db.session.scalars(query).all()

    serialized_dates = []

    for date in all_dates:
        item = {
            "id": date.id,
            "full_date": date.full_date,
            "day_name": date.day_name,
            "day_of_week": date.day_of_week,
            "day_of_month": date.day_of_month,
            "day_of_year": date.day_of_year,
            "month_name": date.month_name,
            "month_of_year": date.month_of_year,
            "year_of_date": date.year_of_date,
            "an_event": date.an_event,
            "event_name": date.event_name
        }
        serialized_dates.append(item)

    return jsonify(serialized_dates)


# Retrieve all transactions
@app.route("/transactions", methods=["GET"])
def get_transactions():
    query = sa.select(Transaction)
    all_transactions = db.session.scalars(query).all()

    serialized_transactions = []

    for transaction in all_transactions:
        item = {
            "id": transaction.id,
            "store_id": transaction.store_id,
            "date_id": transaction.date_id,
            "product_id": transaction.product_id,
            "sales_qty": transaction.sales_qty,
            "unit_cost": transaction.unit_cost,
            "regular_unit_price": transaction.regular_unit_price,
            "discount_unit_price": transaction.discount_unit_price,
            "net_unit_price": transaction.net_unit_price,
            "extended_discount_dollar_amount": transaction.extended_discount_dollar_amount,
            "extended_sales_dollar_amount": transaction.extended_sales_dollar_amount,
            "extended_cost_dollar_amount": transaction.extended_cost_dollar_amount,
            "extended_gross_profit_dollar_amount": transaction.extended_gross_profit_dollar_amount,
            "created_at": transaction.created_at,
        }
        serialized_transactions.append(item)

    return jsonify(serialized_transactions)