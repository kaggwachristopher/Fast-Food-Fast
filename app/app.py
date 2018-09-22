from flask import Flask, jsonify, request, json
import datetime
import random
from instance.config import DevelopmentConfig

app = Flask(__name__)
all_orders_list = []


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'API endpoint, type /api/v1/orders to get all orders'})


@app.route('/api/v1/orders', methods=['POST'])
def place_an_order():
    data = request.get_json()
    user_id = data['user_id']
    recipe_id = data['recipe_id']
    quantity = data['quantity']
    order_id = len(all_orders_list) + 1

    #    order_id = int(random.uniform(100, 99999))
    new_order = {
          "user_id": user_id,
          "quantity": quantity,
          "recipe_id": recipe_id,
          "order_id": order_id,
          "order_status": "Pending",
          "order_date": str(datetime.datetime.now())
                }
    all_orders_list.append(new_order)
    return jsonify({'order': new_order}),201


@app.route('/api/v1/orders', methods=['GET'])
def all_orders_getter():
    return jsonify({'orders': all_orders_list}), 200


@app.route('/api/v1/orders/<order_id>', methods=['GET'])
def get_an_order(order_id):
    for order in all_orders_list:
        if str(order['order_id']) == str(order_id):
            return jsonify(order), 200
    return jsonify({'error': 'Order does not exist not'}), 404


@app.route('/api/v1/orders/<order_id>', methods=['PUT'])
def update_an_order(order_id):
    data = request.get_json()
    status_id = data['status_id']

    if type(status_id) != int:
        return jsonify({'error': 'order status has to be a number'}), 403
    if str(status_id).strip() == "":
        return jsonify({'error': 'status_id cannot be empty'}), 403
    for order in all_orders_list:
        if str(order['order_id']) == str(order_id):
            if status_id == 0:
                order['order_status'] = "Declined"
                return jsonify({'status updated': order}), 201
            elif status_id == 1:
                order['order_status'] = "Pending"
                return jsonify({'status updated': order}), 201
            elif status_id == 2:
                order['order_status'] = "Accepted"
                return jsonify({'status updated': order}), 201
            elif status_id == 3:
                order['order_status'] = "Completed"
                return jsonify({'status updated': order}), 201
            else:
                return jsonify({'message':'invalid status_id entry'})

    return jsonify({'Not found': 'invalid order id'}), 404

    '''
    when the status_id is zero,the order status is changed to declined
    when the status_id is 1,the order status is changed to pending
    when the status_id is 2,the order status is changed to Accepted
    when the status_id is 3,the order status is changed to Completed
    '''