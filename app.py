from flask import Flask, render_template, request, send_file
import pandas as pd
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from matplotlib import pyplot as plt
import threading

app = Flask(__name__)

app.config['SECRET_KEY'] = 'DataWarehouse' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/pos-3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/generate_chart", methods=['POST'])
def generate_chart():
    chart_type = request.form.get('chart_type')
    chart_title = ""

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

    # Eksekusi query dan ambil data
    data = pd.read_sql(query, db.engine)

    # Buat grafik dalam thread terpisah
    def create_plot():
        plt.clf()  # Reset the current figure
        plt.bar(data['x'], data['y'])
        plt.xlabel('X Label')
        plt.ylabel('Y Label')
        plt.title(chart_title)
        chart_filename = 'static/chart.png'
        plt.savefig(chart_filename)
    
    plot_thread = threading.Thread(target=create_plot)
    plot_thread.start()
    plot_thread.join()  # Menunggu thread selesai

    return render_template('index.html', chart='static/chart.png')

if __name__ == "__main__":
    app.run(debug=True)
