# How to start REST API

1. Create a Python virtual environment

```
pip install virtualenv
python -m venv venv
```

2. Start virtual environment (macOS & Windows)
   a. MacOS

```
source venv/bin/activate
```

b. Windows

```
venv/Scripts/activate
```

3. Install all packages/libraries required

```
pip install -r requirements.txt
```

4. Create .flaskenv file and put this inside:

```
FLASK_APP=data_warehouse.py
```

5. Edit config.py to configure MySQL Database Server

```
import os

class Config(object):
    # Perhatiin @127.0.0.1:port_number
    # Gw pake 3307, karena port 3306 udah kepake
    # Defaultnya biasanya 3306
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1:3307/data_warehouse"
```

6. Create database

```
Database Name : data_warehouse
```

7. Create database & migrate changes from SQLAlchemy models

```
flask db migrate
flask db upgrade
```

8. Run REST API server in debug mode (to automatically apply code changes)

```
flask run --debug
```

Additionals:

1. To apply changes made to database models to table in database server, always run:

```
flask db migrate
flask db upgrade
```

2. To run python (flask) shell

```
flask shell
```
