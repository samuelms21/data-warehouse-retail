from app import app, db
from flask import jsonify, request, make_response
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


# Quantity of Items Sold
@app.route("/qty_items_sold", methods=["GET"])
def get_qty_of_items_sold():
    """
    Required parameter: date_id (or just date)

    groupby (optional): mau di groupby berdasarkan apa -> "store" or "product"

    store_id
    product_id

    If both "store_id" and "product_id" are provided: 
    -> Berapa total jumlah item yang terjual untuk produk {product_id} di toko {store_id} pada tanggal {date_id}
    -> Ex: {{BASE_URL}}/qty_items_sold?date_id=e6137ef3-b92b-4c7d-aa93-3ffdccf1f030&store_id=c7fda58c-aa0c-4766-b21f-7eb8a388bdd0&product_id=e08cbee7-4ceb-4d48-9b22-3690833ed5fa
    -> group_by = None (emang ga perlu untuk query ini)
    -> store_id = c7fda58c-aa0c-4766-b21f-7eb8a388bdd0
    -> product_id = e08cbee7-4ceb-4d48-9b22-3690833ed5fa
    
    SQL Query if group_by = store:
    SELECT
        dates.full_date,
        stores.name AS store_name,
        SUM(transactions.sales_qty) AS total_sales_qty
    FROM
        stores
    INNER JOIN transactions ON stores.id = transactions.store_id
    INNER JOIN dates ON transactions.date_id = dates.id
    WHERE
        dates.id = "e6137ef3-b92b-4c7d-aa93-3ffdccf1f030"
        
        -- if store_id is provided:
        -- kemayoran store
        -- AND stores.id = "c7fda58c-aa0c-4766-b21f-7eb8a388bdd0"
        
        -- bekasi store
        -- AND stores.id = "2e67025f-29bd-4861-b4d2-2fa0d780564a"

    GROUP BY stores.id;

    Ex 1: {{BASE_URL}}/qty_items_sold?group_by=store&date_id=e6137ef3-b92b-4c7d-aa93-3ffdccf1f030
    -> group_by = store
    -> date_id = e6137ef3-b92b-4c7d-aa93-3ffdccf1f030
    -> Return total jumlah item yang terjual di masing-masing toko yang sudah merekam transaksi pada tanggal {date_id}

    Ex 2: {{BASE_URL}}/qty_items_sold?group_by=store&date_id=e6137ef3-b92b-4c7d-aa93-3ffdccf1f030&store_id=c7fda58c-aa0c-4766-b21f-7eb8a388bdd0
    -> group_by = store
    -> date_id = e6137ef3-b92b-4c7d-aa93-3ffdccf1f030
    -> store_id = c7fda58c-aa0c-4766-b21f-7eb8a388bdd0
    -> Return total jumlah item yang terjual pada toko {store_id} pada tanggal {date_id}

    
    SQL Query if group_by = product
    SELECT
        dates.full_date,
        products.name AS product_name,
        products.brand AS product_brand,
        products.category AS product_category,
        products.department AS product_department,
        SUM(transactions.sales_qty) AS total_sales_qty
    FROM
        products
    INNER JOIN transactions ON products.id = transactions.product_id
    INNER JOIN dates ON transactions.date_id = dates.id
    WHERE
        dates.id = "e6137ef3-b92b-4c7d-aa93-3ffdccf1f030"
        
        -- if product_id is provided:
        -- mentega
        -- AND products.id = "e08cbee7-4ceb-4d48-9b22-3690833ed5fa"

        -- sikat gigi (dan seterusnya)
        -- AND products.id = "7ce11f04-c3ec-455a-82cc-15385fa09a87"

    GROUP BY
        products.id;

    Ex 3: {{BASE_URL}}/qty_items_sold?group_by=product&date_id=e6137ef3-b92b-4c7d-aa93-3ffdccf1f030
    -> group_by = product
    -> date_id = e6137ef3-b92b-4c7d-aa93-3ffdccf1f030
    -> Return total jumlah item yang terjual untuk setiap produk yang ada pada tanggal {date_id}

    Ex 4: {{BASE_URL}}/qty_items_sold?group_by=product&date_id=e6137ef3-b92b-4c7d-aa93-3ffdccf1f030&product_id=e08cbee7-4ceb-4d48-9b22-3690833ed5fa
    -> group_by = product
    -> date_id = e6137ef3-b92b-4c7d-aa93-3ffdccf1f030
    -> product_id = e08cbee7-4ceb-4d48-9b22-3690833ed5fa
    -> Return total jumlah item yang terjual untuk produk {product_id} pada tanggal {date_id}
    """

    # Mungkin date_id bakalan susah dibaca (karena pake UUID)
    # Saran (sam): Mungkin kita pake full_date aja
    date_id = request.args.get("date_id")
    
    if not date_id:
        error_response = make_response(jsonify({"error": "Bad Request. Date ID not provided."}, 400))
        return error_response
    
    groupby = request.args.get("group_by")
    product_id = request.args.get("product_id")
    store_id = request.args.get("store_id")


    if groupby == "store":
        if store_id:
            query = db.session.query(
                    DateModel.full_date,
                    Store.name.label('store_name'),
                    db.func.sum(Transaction.sales_qty).label('total_sales_qty')
                ).join(Transaction, DateModel.id == Transaction.date_id).join(Store, Store.id == Transaction.store_id).filter(DateModel.id == date_id).filter(Store.id == store_id).first()
            
            serialized_result = {
                "full_date": query.full_date.strftime('%B %d, %Y'),
                "store_name": query.store_name,
                "total_sales_qty": query.total_sales_qty
            }

            return jsonify(serialized_result)

        else:    
            query = db.session.query(
                    DateModel.full_date,
                    Store.name.label('store_name'),
                    db.func.sum(Transaction.sales_qty).label('total_sales_qty')
                ).join(Transaction, DateModel.id == Transaction.date_id).join(Store, Store.id == Transaction.store_id).filter(DateModel.id == date_id).group_by(Store.id).all()
            
            serialized_results = []

            for row in query:
                item = {
                    "full_date": row.full_date.strftime('%B %d, %Y'),
                    "store_name": row.store_name,
                    "total_sales_qty": row.total_sales_qty
                }
                serialized_results.append(item)

            return jsonify(serialized_results)

    if groupby == "product":
        if product_id:
            query = db.session.query(
                        DateModel.full_date,
                        Product.name.label('product_name'),
                        Product.brand.label('product_brand'),
                        Product.category.label('product_category'),
                        Product.department.label('product_department'),
                        db.func.sum(Transaction.sales_qty).label('total_sales_qty')
                    ).join(Transaction, Product.id == Transaction.product_id).join(DateModel, Transaction.date_id == DateModel.id).filter(DateModel.id == date_id).filter(Product.id == product_id).group_by(Product.id).first()
            
            serialized_result = {
                "full_date": query.full_date,
                "product_name": query.product_name,
                "product_brand": query.product_brand,
                "product_category": query.product_category,
                "product_department": query.product_department,
                "total_sales_qty": query.total_sales_qty,
            }

            return jsonify(serialized_result)

        else:
            query = db.session.query(
                        DateModel.full_date,
                        Product.name.label('product_name'),
                        Product.brand.label('product_brand'),
                        Product.category.label('product_category'),
                        Product.department.label('product_department'),
                        db.func.sum(Transaction.sales_qty).label('total_sales_qty')
                    ).join(Transaction, Product.id == Transaction.product_id).join(DateModel, Transaction.date_id == DateModel.id).filter(DateModel.id == date_id).group_by(Product.id).all()
            
            serialized_results = []
            for row in query:
                item = {
                    "full_date": row.full_date,
                    "product_name": row.product_name,
                    "product_brand": row.product_brand,
                    "product_category": row.product_category,
                    "product_department": row.product_department,
                    "total_sales_qty": row.total_sales_qty,
                }
                serialized_results.append(item)

            return jsonify(serialized_results)

    if not groupby:
        if not product_id or not store_id:
            error_response = make_response(jsonify({"error": "Both product_id and store_id have to be provided for this case."}, 400))
            return error_response
        
        query = db.session.query(
                    DateModel.full_date,
                    Store.name.label('store_name'),
                    Product.name.label('product_name'),
                    Product.brand.label('product_brand'),
                    Product.category.label('product_category'),
                    Product.department.label('product_department'),
                    db.func.sum(Transaction.sales_qty).label('total_sales_qty')
                ).join(Transaction, Product.id == Transaction.product_id).join(DateModel, Transaction.date_id == DateModel.id).join(Store, Transaction.store_id == Store.id).filter(DateModel.id == date_id).filter(Product.id == product_id).filter(Store.id == store_id).group_by(Product.id).all()
        
        serialized_result = {
            "full_date": query.full_date,
            "store_name": query.store_name,
            "product_name": query.product_name,
            "product_brand": query.product_brand,
            "product_category": query.product_category,
            "product_department": query.product_department,
            "total_sales_qty": query.total_sales_qty,
        }

        return jsonify(serialized_result)

    return {"message": "testing route qty_items_sold"}


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


