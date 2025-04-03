from flask import Flask, request, jsonify
from myapp.models import Product

app = Flask(__name__)

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.get(product_id)
    return jsonify(product.to_dict()) if product else ("Not Found", 404)

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.json
    product = Product.update(product_id, data)
    return jsonify(product.to_dict()) if product else ("Not Found", 404)

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    success = Product.delete(product_id)
    return ("Deleted", 204) if success else ("Not Found", 404)

@app.route("/products", methods=["GET"])
def list_all_products():
    products = Product.list_all()
    return jsonify([p.to_dict() for p in products])

@app.route("/products", methods=["GET"])
def list_by_filter():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")
    products = Product.filter(name=name, category=category, available=available)
    return jsonify([p.to_dict() for p in products])
