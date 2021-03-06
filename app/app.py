from flask import Flask, jsonify, request, json
from app.models import RecipeOrders

app = Flask(__name__)
recipe = RecipeOrders()


@app.route('/api/v1/orders', methods=['POST'])
def place_an_order():
    if recipe.invalid_order():
        return recipe.invalid_order()
    else:
        return recipe.place_order()


@app.route('/api/v1/orders', methods=['GET'])
def all_orders_getter():
    return recipe.get_all_orders()


@app.route('/api/v1/orders/<order_id>', methods=['GET'])
def get_an_order(order_id):
    return recipe.get_single_order(order_id)


@app.route('/api/v1/orders/<order_id>', methods=['PUT'])
def update_an_order(order_id):
    if recipe.invalid_update():
        return recipe.invalid_update()
    else:
        return recipe.update_order_status(order_id)
