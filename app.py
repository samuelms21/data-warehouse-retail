from flask import Flask, render_template, request, send_file
import pandas as pd
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import threading
import time


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



if __name__ == "__main__":
    app.run(debug=True)
