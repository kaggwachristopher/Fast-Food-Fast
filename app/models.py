from flask import jsonify, request
import datetime


class RecipeOrders:

    def __init__(self):
        self.all_orders_list = [ {
            "order_date": "2018-09-22 02:36:27.956913",
            "order_id": 3,
            "order_status": "Pending",
            "quantity": "5",
            "recipe_id": "4",
            "user_id": "21"
        }]

    def place_order(self):
        data = request.get_json()
        user_id = data['user_id']
        recipe_id = data['recipe_id']
        quantity = data['quantity']
        order_id = len(self.all_orders_list) + 1
        new_order = {
            "user_id": user_id,
            "quantity": quantity,
            "recipe_id": recipe_id,
            "order_id": order_id,
            "order_status": "Pending",
            "order_date": str(datetime.datetime.now())
        }
        self.all_orders_list.append(new_order)
        return jsonify({'order': new_order}), 201

    def get_all_orders(self):
        return jsonify({'orders': self.all_orders_list}), 200

    def get_single_order(self,order_id):
        for order in self.all_orders_list:
            if str(order['order_id']) == str(order_id):
                return jsonify(order), 200
        return jsonify({'error': 'Order does not exist not'}), 404
        pass

    def update_order_status(self, order_id):
        data = request.get_json()
        status_id = data['status_id']

        if type(status_id) != int:
            return jsonify({'error': 'order status has to be a number'}), 403
        else:
            pass
        if str(status_id).strip() == "":
            return jsonify({'error': 'status_id cannot be empty'}), 403
        for order in self.all_orders_list:
            if str(order['order_id']) == str(order_id):
                if status_id == 0:
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
                    return jsonify({'message': 'invalid status_id entry'}), 403

        return jsonify({'Not found': 'invalid order id'}), 404
