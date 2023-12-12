from app import app

# Function index() will run when request is made to "/" or "/index"
@app.route("/")
@app.route("/index")
def index():
    return "Hello World"

@app.route("/products/{product_id}/")
def get_products(product_id):
    pass