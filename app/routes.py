from app import app, db
from flask import jsonify, request, make_response
import sqlalchemy as sa
from app.models import Product, Store, DateModel, Transaction

@app.route("/")
@app.route("/index")
def index():
    return "Hello World"

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


### QUANTITY OF ITEMS SOLD

@app.route("/qty_items_sold", methods=["GET"])
def get_qty_of_items_sold():
    # Get the date_id from the request parameters
    date_id = request.args.get("date_id")
    # If date_id is not provided, return an error response
    if not date_id:
        return make_response(jsonify({"error": "Bad Request. Date ID not provided."}), 400)
    
    # Get the group_by, product_id, and store_id parameters from the request
    groupby = request.args.get("group_by")
    product_id = request.args.get("product_id")
    store_id = request.args.get("store_id")

    # Handle the request based on the group_by parameter
    if groupby == "store":
        return handle_store_group(date_id, store_id)
    elif groupby == "product":
        return handle_product_group(date_id, product_id)
    elif not groupby and product_id and store_id:
        return handle_no_group(date_id, product_id, store_id)
    else:
        return make_response(jsonify({"error": "Invalid request parameters."}), 400)

# Handle the case where group_by is "store"
def handle_store_group(date_id, store_id):
    # Build the query
    query = db.session.query(
        Store.id.label('store_id'),
        DateModel.full_date.label('full_date'),
        Store.name.label('store_name'),
        db.func.sum(Transaction.sales_qty).label('total_sales_qty')
    ).join(Transaction, DateModel.id == Transaction.date_id).join(Store, Store.id == Transaction.store_id).filter(DateModel.id == date_id)

    # If store_id is provided, filter by store_id
    if store_id:
        query = query.filter(Store.id == store_id)
    # If store_id is not provided, group by store_id
    else:
        query = query.group_by(Store.id)

    # Serialize the results and return them as a JSON response
    return jsonify(serialize_store_results(query.all()))

# Handle the case where group_by is "product"
def handle_product_group(date_id, product_id):
    # Build the query
    query = db.session.query(
        DateModel.full_date.label('full_date'),
        Product.id.label('product_id'),
        Product.name.label('product_name'),
        Product.brand.label('product_brand'),
        Product.category.label('product_category'),
        Product.department.label('product_department'),
        db.func.sum(Transaction.sales_qty).label('total_sales_qty')
    ).join(Transaction, Product.id == Transaction.product_id).join(DateModel, Transaction.date_id == DateModel.id).filter(DateModel.id == date_id)

    # If product_id is provided, filter by product_id
    if product_id:
        query = query.filter(Product.id == product_id)
    # If product_id is not provided, group by product_id
    else:
        query = query.group_by(Product.id)

    # Serialize the results and return them as a JSON response
    return jsonify(serialize_product_results(query.all()))

# Handle the case where group_by is not provided but product_id and store_id are
def handle_no_group(date_id, product_id, store_id):
    # Build the query
    query = db.session.query(
        DateModel.full_date,
        Store.id.label('store_id'),
        Store.name.label('store_name'),
        Product.id.label('product_id'),
        Product.name.label('product_name'),
        Product.brand.label('product_brand'),
        Product.category.label('product_category'),
        Product.department.label('product_department'),
        db.func.sum(Transaction.sales_qty).label('total_sales_qty')
    ).join(Transaction, Product.id == Transaction.product_id).join(DateModel, Transaction.date_id == DateModel.id).join(Store, Transaction.store_id == Store.id).filter(DateModel.id == date_id).filter(Product.id == product_id).filter(Store.id == store_id)

    # Serialize the results and return them as a JSON response
    return jsonify(serialize_product_store_results(query.all()))

# Serialize the results for the case where group_by is "store"
def serialize_store_results(results):
    return [
        {
            "store_id": row.store_id,
            "full_date": row.full_date.strftime('%B %d, %Y'),
            "store_name": row.store_name,
            "total_sales_qty": row.total_sales_qty
        } for row in results
    ]

# Serialize the results for the case where group_by is "product" or not provided
def serialize_product_results(results):
    return [
        {
            "product_id": row.product_id,
            "full_date": row.full_date.strftime('%B %d, %Y'),
            "product_name": row.product_name,
            "product_brand": row.product_brand,
            "product_category": row.product_category,
            "product_department": row.product_department,
            "total_sales_qty": row.total_sales_qty,
        } for row in results
    ]


# Serialize the results for the case where group_by is "product" or not provided
def serialize_product_store_results(results):
    return [
        {
            "store_id": row.store_id,
            "store_name": row.store_name,
            "product_id": row.product_id,
            "full_date": row.full_date.strftime('%B %d, %Y'),
            "product_name": row.product_name,
            "product_brand": row.product_brand,
            "product_category": row.product_category,
            "product_department": row.product_department,
            "total_sales_qty": row.total_sales_qty,
        } for row in results
    ]

### QUANTITY OF ITEMS SOLD


### TOTAL SALES
@app.route("/total_sales", methods=["GET"])
def get_total_sales():
    """
    Required parameters: date_id OR (start_date_id && end_date_id)

    Bisa request untuk date range (jangka waktu tertentu) atau single date (satu hari saja)
    Contoh date range: Total Sales semua toko sejak tgl 1 Jan 2024 s.d. 5 Jan 2024
    Contoh single date: Total Sales semua toko pada tanggal 1 Jan 2024 (saja)

    Date Range Mode
    start_date_id : ID of start date
    end_date_id: ID of end date

    Single Date Mode:
    date_id: ID of date to calculate total sales

    Other parameters:
    - groupby: "product" or "store"
    - product_id
    - store_id
    """

    groupby = request.args.get("group_by")
    date_id = request.args.get("date_id")
    start_date_id = request.args.get("start_date_id")
    end_date_id = request.args.get("end_date_id")


    if groupby == "product":

        # Berarti total sales per produk untuk 1 hari saja
        if date_id:
            """
            SQL Query
            SELECT
                products.id AS product_id
                products.name AS product_name,
                products.brand AS product_brand,
                products.category AS product_category,
                products.department AS product_department,
                SUM(transactions.extended_sales_dollar_amount) AS total_sales_dollar_amount
            FROM
                products
            INNER JOIN transactions ON products.id = transactions.product_id
            INNER JOIN dates ON transactions.date_id = dates.id
            WHERE
                dates.id = '{some_date_id}'
            GROUP BY
                products.id;
            """
            results = db.session.query(
                        DateModel.full_date.label("full_date"),
                        Product.id.label('product_id'),
                        Product.name.label('product_name'),
                        Product.brand.label('product_brand'),
                        Product.category.label('product_category'),
                        Product.department.label('product_department'),
                        db.func.sum(Transaction.extended_sales_dollar_amount).label('total_sales_dollar_amount')
                    ).join(
                        Transaction, Product.id == Transaction.product_id
                    ).join(
                        DateModel, Transaction.date_id == DateModel.id
                    ).filter(
                        DateModel.id == date_id
                    ).group_by(
                        Product.id
                    ).all()
            
            serialized_results = []
            
            for row in results:
                item = {
                    "full_date": row.full_date.strftime('%B %d, %Y'),
                    "product_id": row.product_id,
                    "product_name": row.product_name,
                    "product_brand": row.product_brand,
                    "product_category": row.product_category,
                    "product_department": row.product_department,
                    "total_sales_dollar_amount": row.total_sales_dollar_amount
                }
                serialized_results.append(item)

            return jsonify(serialized_results)
        
        # Berarti total sales per produk untuk jangka waktu tertentu
        if start_date_id and end_date_id:
            """
            SQL Query:
            SELECT
                products.id AS product_id,
                products.name AS product_name,
                products.brand AS product_brand,
                products.category AS product_category,
                products.department AS product_department,
                SUM(transactions.extended_sales_dollar_amount) AS total_sales_dollar_amount
            FROM
                products
            INNER JOIN transactions ON products.id = transactions.product_id
            INNER JOIN dates ON transactions.date_id = dates.id
            WHERE
                dates.full_date >= (
                    SELECT full_date
                    FROM dates
                    WHERE id = '{start_date_id}'
                )
                AND dates.full_date <= (
                    SELECT full_date
                    FROM dates
                    WHERE id = '{end_date_id}
                )
            GROUP BY
                products.id;
            """
            results = db.session.query(
                Product.id.label('product_id'),
                Product.name.label('product_name'),
                Product.brand.label('product_brand'),
                Product.category.label('product_category'),
                Product.department.label('product_department'),
                db.func.sum(Transaction.extended_sales_dollar_amount).label('total_sales_dollar_amount')
            ).join(Transaction, Product.id == Transaction.product_id) \
            .join(DateModel, Transaction.date_id == DateModel.id) \
            .filter(DateModel.full_date.between(
                db.session.query(DateModel.full_date).filter(DateModel.id == start_date_id),
                db.session.query(DateModel.full_date).filter(DateModel.id == end_date_id)
            )).group_by(Product.id).all()

            # Extracting values into a list of dictionaries
            result_list = [
                {
                    'product_id': result.product_id,
                    'product_name': result.product_name,
                    'product_brand': result.product_brand,
                    'product_category': result.product_category,
                    'product_department': result.product_department,
                    'total_sales_dollar_amount': result.total_sales_dollar_amount
                }
                for result in results
            ]

            return jsonify(result_list)

    if groupby == "store":

        # Berarti total sales per toko untuk 1 hari saja
        if date_id:
            """
            SQL Query:
            SELECT
                stores.id AS store_id
                stores.name AS store_name,
                SUM(transactions.extended_sales_dollar_amount) AS total_sales_dollar_amount
            FROM
                stores
            INNER JOIN transactions ON stores.id = transactions.store_id
            INNER JOIN dates ON transactions.date_id = dates.id
            WHERE
                dates.id = "{some_date_id}"
            GROUP BY
                stores.id;
            """
            results = db.session.query(
                            Store.id.label("store_id"),
                            Store.name.label("store_name"),
                            db.func.sum(Transaction.extended_sales_dollar_amount).label('total_sales_dollar_amount')
                        ).join(Transaction, Store.id == Transaction.store_id) \
                        .join(DateModel, Transaction.date_id == DateModel.id) \
                        .filter(DateModel.id == date_id) \
                        .group_by(Store.id).all()

            # Extracting values into a list of dictionaries
            result_list = [
                {
                    'store_id': result.store_id,
                    'store_name': result.store_name,
                    'total_sales_dollar_amount': result.total_sales_dollar_amount
                }
                for result in results
            ]

            return jsonify(result_list)
        
        # Berarti total sales per toko untuk jangka waktu tertentu
        if start_date_id and end_date_id:
            """
            SQL Query:
            SELECT
                stores.id AS store_id,
                stores.name AS store_name,
                SUM(transactions.extended_sales_dollar_amount) AS total_sales_dollar_amount
            FROM
                stores
            INNER JOIN transactions ON stores.id = transactions.store_id
            INNER JOIN dates ON transactions.date_id = dates.id
            WHERE
                dates.full_date >= (
                    SELECT full_date
                    FROM dates
                    WHERE id = '{start_date_id}'
                )
                AND dates.full_date <= (
                    SELECT full_date
                    FROM dates
                    WHERE id = '{end_date_id}'
                )
            GROUP BY
                stores.id;
            """
            results = db.session.query(
                Store.id.label('store_id'),
                Store.name.label('store_name'),
                db.func.sum(Transaction.extended_sales_dollar_amount).label('total_sales_dollar_amount')
            ).join(Transaction, Store.id == Transaction.store_id) \
            .join(DateModel, Transaction.date_id == DateModel.id) \
            .filter(DateModel.full_date.between(
                db.session.query(DateModel.full_date).filter(DateModel.id == start_date_id),
                db.session.query(DateModel.full_date).filter(DateModel.id == end_date_id)
            )).group_by(Store.id).all()

            # Extracting values into a list of dictionaries
            result_list = [
                {
                    'store_id': result.store_id,
                    'store_name': result.store_name,
                    'total_sales_dollar_amount': result.total_sales_dollar_amount
                }
                for result in results
            ]

            return jsonify(result_list)

### TOTAL SALES


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


