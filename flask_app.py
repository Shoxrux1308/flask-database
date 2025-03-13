from flask import Flask, request
from db import ProductsDB


app = Flask(__name__)
db = ProductsDB('products_db.json')

## view all products
@app.route('/products', methods=['GET'])
def get_all_products():
    """Returns all products in the database"""
    res=db.all_products()
    return res

# view all product by id
@app.route('/products/id/<id>', methods=['GET'])
def get_all_product(id):
    """Returns product in the database by id"""
    res=db.get_product_id(id)
    return res

# view all ptoducts names
@app.route('/products/names', methods=['GET'])
def get_product_all_names():
    """Returns all product names"""
    res=db.get_all_product_names()
    return res


# view products by name
@app.route('/productss/name/<name>', methods=['GET'])
def get_products_by_name(name):
    """Returns a product by name"""
    res=db.get_names(name)
    return res

# view all ptoducts catagories
@app.route('/products/catagories', methods=['GET'])
def get_product_all_catagories():
    """Returns all product catagories"""
    res=db.get_all_catagories()
    return res

# view products by price
@app.route('/products/price/<price>', methods=['GET'])
def get_products_by_price(price):
    """Returns a product by price"""
    res=db.get_small_from_price(price)
    return res

# view products expensive
@app.route('/products/price/top/expensive', methods=['GET'])
def get_products_expensive():
    """Returns a top three expensive products"""
    res=db.expensive_products()
    return res

# view products between max_price and min_price
@app.route('/products/price/between', methods=['GET'])
def get_between_price():
    """Returns a products between max_price and min_price
    get max_price and min_price from query_string
    """
    res=db.get_between_price(request.args.get('max_price'), request.args.get('min_price'))
    return res

# view add product
@app.route('/products/add', methods=['POST'])
def add_products():
    """Adds a product to the database"""
    data = request.get_json()
    return db.add_product(data)


# view delete product
@app.route('/products/delete/<doc_id>', methods=['DELETE'])
def delete_product(doc_id):
    """Deletes a product from the database"""
    res=db.delete_product(doc_id)
    return {
        "message": "Product deleted successfully"
    }


if __name__ == '__main__':
    app.run(debug=True)