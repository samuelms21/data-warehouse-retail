from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, send_file
import pandas as pd
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading
import time
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.static_folder = 'static'

db = SQLAlchemy(app)

@app.route("/")
def index():
    query_all_stores = "SELECT id,name FROM store"
    query_all_products = "SELECT id,name FROM product"
    query_all_date = "SELECT id,full_date FROM date"
    
    stores = pd.read_sql(query_all_stores, db.engine)
    products = pd.read_sql(query_all_products, db.engine)
    dates = pd.read_sql(query_all_date, db.engine)

    return render_template('index.html', stores=stores.to_dict(orient='records'), products=products.to_dict(orient='records'), dates=dates.to_dict(orient='records'))
    

@app.route("/generate_chart", methods=['POST'])
def generate_chart():
    chart_type = request.form.get('chart_type')
    chart_title = ""
    query = ""

    if chart_type == 'per_toko':
        chart_title = 'Keuntungan Bersih Per Toko'
        query = """
            SELECT store.name AS x, 
                   SUM(product.price * transaction_details.qty) - SUM(product.init_price * transaction_details.qty) AS y
            FROM product
            INNER JOIN transaction_details ON product.id = transaction_details.product_id
            INNER JOIN transaction ON transaction.id = transaction_details.transaction_id
            INNER JOIN store ON store.id = transaction.store_id
            GROUP BY store.name
        """
    elif chart_type == 'per_hari':
        chart_title = 'Keuntungan Bersih Per Hari'
        query = """
            SELECT date.date AS x, 
                   SUM(product.price * transaction_details.qty) - SUM(product.init_price * transaction_details.qty) AS y
            FROM product
            INNER JOIN transaction_details ON product.id = transaction_details.product_id
            INNER JOIN transaction ON transaction.id = transaction_details.transaction_id
            INNER JOIN date ON date.id = transaction.date_id
            GROUP BY date.date
        """
    elif chart_type == 'per_barang':
        chart_title = 'Keuntungan Bersih Per Jenis Barang'
        query = """
            SELECT product.name AS x, 
                   SUM(product.price * transaction_details.qty) - SUM(product.init_price * transaction_details.qty) AS y
            FROM product
            INNER JOIN transaction_details ON product.id = transaction_details.product_id
            GROUP BY product.name
        """

    # Ini buat eksekusi query sama ambil data aja
    data = pd.read_sql(query, db.engine)

    # Buat grafik dalam thread terpisah sama nama file unik
    def create_3d_plot():
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.bar(data['x'], data['y'], zs=0, zdir='y', alpha=0.8)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        ax.set_title(chart_title)
        chart_filename = f'static/chart_{chart_type}_{int(time.time())}.png'
        plt.savefig(chart_filename)


    plot_thread = threading.Thread(target=create_3d_plot)  # Ubah doang dari create_plot jadi create_3d_plot
    plot_thread.start()
    plot_thread.join()


    return render_template('index.html', chart=f'static/chart_{chart_type}_{int(time.time())}.png')

@app.route("/visualize_data", methods=['POST'])
def visualize_data():
    selected_store = request.form.get('select_store')
    selected_product = request.form.get('select_product')
    selected_date = request.form.get('select_date')


if __name__ == "__main__":
    app.run(debug=os.environ.get('DEBUG'))
