# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@localhost:3306/data_warehouse"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "data-warehouse-key"
