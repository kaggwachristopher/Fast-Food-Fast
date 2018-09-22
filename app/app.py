from flask import jsonify, request, json
import datetime
import random

if __name__ == '__main__':
    import app

all_orders_list = []


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API endpoint, type /api/v1/orders to get all orders'})


@app.route('/api/v1/orders',methods=['POST'])
def place_an_order():
    data = request.get_json()
    user_id = data['user_id']
    recipe_id = data['recipe_id']
    quantity = data['quantity']
    order_id = int(random.uniform(100, 99999))
    new_order = {
          "user_id": user_id,
          "quantity": quantity,
          "recipe_id":recipe_id,
          "order_id":order_id,
          "order_status":"Pending",
          "order_date":str(datetime.datetime.now())
                }
    all_orders_list.append(new_order)
    return jsonify({'order': new_order}),201


@app.route('/api/v1/orders', methods=['GET'])
def all_orders_getter():
    return jsonify({'orders' : all_orders_list}), 200


@app.route('/api/v1/orders/<order_id>', methods=['GET'])
def get_an_order(order_id):
    for order in all_orders_list:
        if str(order['order_id']) == str(order_id):
            return jsonify(order), 200
    return jsonify({'error': 'Order does not exist not'}), 404