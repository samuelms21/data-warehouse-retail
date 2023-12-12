import os

class Config(object):
    # Perhatiin @127.0.0.1:port_number
    # Gw pake 3307, karena port 3306 udah kepake
    # Defaultnya biasanya 3306
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1:3306/data_warehouse"