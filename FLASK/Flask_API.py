from enum import unique
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 


app  = Flask(__name__)
app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///products.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#init db
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name 
        self.description = description
        self.price = price
        self. quantity = quantity
    
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

#Init shema
product_shema = ProductSchema()
products_shema = ProductSchema(many=True)

@app.route('/product', methods = ['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['quantity']

    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()
    return product_shema.jsonify(new_product)
#get all product
@app.route('/products', methods = ['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_shema.dump(all_products)
    return jsonify(result)
@app.route('/product/<id>', methods = ['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_shema.jsonify(product)

@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_shema.jsonify(product)

@app.route('/product/<id>', methods = ['PUT'])
def update_product(id):
    product = Product.query.get(id)
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['quantity']
    print(product)
    if name:
        product.name = name
    if description:
        product.description = name
    if price:
        product.price = price
    if qty:
        product.quantity = qty
    db.session.commit()
    return product_shema.jsonify(product)
# Run Server
if __name__ == '__main__':
    app.run(debug=True)