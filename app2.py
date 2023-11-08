from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import seaborn as sns
import pandas as pd
import numpy as np
import threading
import os


# initialization
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.static_folder = "static"
db = SQLAlchemy(app)


def get_chart(x: list[str], y: list[str], z: list[float], storeId: str):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Define positions
    xunique = {j: i for i, j in enumerate(set(x))}
    yunique = {j: i for i, j in enumerate(set(y))}
    xpos = [xunique[i] for i in x]
    ypos = [yunique[i] for i in y]
    zpos = np.zeros_like(xpos)
    dx = dy = 0.9
    dz = z

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

    ax.set_xticks(np.arange(len(xunique.keys())))
    ax.set_yticks(np.arange(len(yunique.keys())))
    ax.set_xticklabels(xunique.keys())
    ax.set_yticklabels(yunique.keys())

    ax.set_xlabel("Date")
    ax.set_ylabel("Name")
    ax.set_zlabel("Profit")
    plt.title(f"Profit in Store-{storeId}")
    plt.show()


def get_chart(
    x: list[str],
    y: list[str],
    z: list[float],
    labels: list[str],
    subject: str,
    storeId: str,
):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Define positions
    xunique = {j: i for i, j in enumerate(set(x))}
    yunique = {j: i for i, j in enumerate(set(y))}
    xpos = [xunique[i] for i in x]
    ypos = [yunique[i] for i in y]
    zpos = np.zeros_like(xpos)
    dx = dy = 0.9
    dz = z

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True)

    ax.set_xticks(np.arange(len(xunique.keys())))
    ax.set_yticks(np.arange(len(yunique.keys())))
    ax.set_xticklabels(xunique.keys())
    ax.set_yticklabels(yunique.keys())

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])
    plt.title(f"{subject} in Store-{storeId}")
    plt.show()


@app.route("/uc1/<storeid>")
def usecase1(storeid):
    query = f"""
        SELECT date_dimension.date, product.name, sum(sales_facts.net_unit_price*sales_facts.qty)-sum(sales_facts.regular_unit_price*sales_facts.qty) as profit
        FROM product
        INNER JOIN sales_facts ON product.id = sales_facts.product_id
        INNER JOIN date_dimension ON sales_facts.date_id = date_dimension.id
        WHERE sales_facts.store_id = '{storeid}'
        GROUP BY date_dimension.id, product.id
    """
    data = pd.read_sql(query, db.engine)
    get_chart(
        list(data["date"]),
        list(data["name"]),
        list(data["profit"]),
        ["Date", "Product", "Profit"],
        "Profit",
        storeid,
    )
    return render_template("index.html")


@app.route("/uc2/<storeid>")
def usecase2(storeid):
    query = f"""
        SELECT date_dimension.date, product.name,((sum(sales_facts.net_unit_price*sales_facts.qty)-sum(sales_facts.regular_unit_price*sales_facts.qty))/sum(sales_facts.net_unit_price*sales_facts.qty))*100 as margin
        FROM product
        INNER JOIN sales_facts ON product.id = sales_facts.product_id
        INNER JOIN date_dimension ON sales_facts.date_id = date_dimension.id
        WHERE sales_facts.store_id = '{storeid}'
        GROUP BY date_dimension.id, product.id
    """
    data = pd.read_sql(query, db.engine)
    get_chart(
        list(data["date"]),
        list(data["name"]),
        list(data["margin"]),
        ["Date", "Product", "Margin"],
        "Margin",
        storeid,
    )
    return render_template("index.html")


# @app.route("/use-case-1")
# def get_1():
# query =


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG"))
