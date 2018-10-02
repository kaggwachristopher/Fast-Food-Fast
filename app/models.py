from flask import jsonify, request,json
import datetime


class RecipeOrders:

    def __init__(self):
        self.all_orders_list = [{
            "order_date": "2018-09-22 02:36:27.956913",
            "order_id": 3,
            "order_status": "Pending",
            "quantity": 5,
            "food_name": "plain chips",
            "user_id": 21
        }]

    def place_order(self):
        data = request.get_json()
        user_id = data['user_id']
        food_name = data['food_name']
        quantity = data['quantity']
        order_id = len(self.all_orders_list) + 1
        new_order = {
            "user_id": user_id,
            "quantity": quantity,
            "food_name": food_name,
            "order_id": order_id,
            "order_status": "Pending",
            "order_date": str(datetime.datetime.now())
        }
        self.all_orders_list.append(new_order)
        return jsonify({'order': new_order}), 201

    def get_all_orders(self):
        # This if statement checks whether the list contains dummy data then it empties the list
        if len(self.all_orders_list) == 1:
            return jsonify({'orders': []}), 200
        else:
            return jsonify({'orders': self.all_orders_list}), 200

    def get_single_order(self, order_id):
        for order in self.all_orders_list:
            if str(order['order_id']) == str(order_id):
                return jsonify(order), 200
        return jsonify({'error': 'Order does not exist not'}), 404
        pass

    def update_order_status(self, order_id):
        data = request.get_json()
        status_id = data['status_id']
        if type(status_id) != int:
            if str(status_id)=="0":
                pass
            return jsonify({'Bad request': 'order status has to be a number from 1-4'}), 400
        else:
            pass
        if str(status_id).strip() == "":
            return jsonify({'error': 'status_id cannot be empty'}), 400
        for order in self.all_orders_list:
            if str(order['order_id']) == str(order_id):
                if status_id == 4:
                    order['order_status'] = "Declined"
                    return jsonify({'status updated': order}), 201
                # when the status_id is zero,the order status is changed to declined

                elif status_id == 1:
                    order['order_status'] = "Pending"
                    return jsonify({'status updated': order}), 201
                # when the status_id is 1,the order status is changed to pending

                elif status_id == 2:
                    order['order_status'] = "Accepted"
                    return jsonify({'status updated': order}), 201
                # when the status_id is 2,the order status is changed to Accepted

                elif status_id == 3:
                    order['order_status'] = "Completed"
                    return jsonify({'status updated': order}), 201
                # when the status_id is 3,the order status is changed to Completed

                else:
                    return jsonify({'message': 'invalid status_id entry'}), 400

        return jsonify({'Not found': 'invalid order id'}), 404

    def invalid_order(self):

        data = request.get_json()
        user_id = data.get('user_id')
        food_name = data.get('food_name')
        quantity = data.get('quantity')

        if not quantity:
            return jsonify({'missing field': 'input must contain the food quantity'}), 400

        elif type(quantity) != int:
            return jsonify({'error': 'the quantity should be a number'}), 400

        if not food_name:
            return jsonify({'missing field': 'input must contain a the name of the food you want'}), 400
        elif type(food_name) != str:
                return jsonify({'error':'the food_name should be a string'}), 400
        elif food_name.strip() == "":
            return jsonify({'error': 'the food_name field cant be empty'}), 400

        if not user_id:
            return jsonify({'missing field': 'input must contain a user_id'}), 400
        elif type(user_id) != int or not user_id:
            return jsonify({'error': 'the user_id should be a number'}), 400

    def invalid_update(self):
        data = request.get_json()
        status_id = data.get('status_id')
        if not status_id:
            return jsonify({'missing field':'you must put a status_id field'})
