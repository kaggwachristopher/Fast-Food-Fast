import unittest
from app.app import app
from flask import json
from app.models import RecipeOrders

tester = RecipeOrders()


class Testing(unittest.TestCase):

    def setUp(self):
        self.api = app
        self.client = self.api.test_client
        self.order = {
            "order_date": "2018-09-22 02:36:27.956913",
            "order_id": 3,
            "order_status": "Pending",
            "quantity": 5,
            "food_name": "pizza",
            "user_id": 21
        }
        self.update = {
            "status_id": 4
        }
        self.update1 = {
            "status_id": 1
        }
        self.update2 = {
            "status_id": 2
        }
        self.update3 = {
            "status_id": 3
        }
        self.update4 = {
            "status_id": 6543454
        }
        self.update5 = {
            "status_id": "any none integer"
        }
        self.update6 = {
            "status_id": "       "
        }

    def test_place_order(self):
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(self.order))
        self.assertEqual(result.status_code, 201)

    def test_single_order_getter(self):
        result = self.client().get('/api/v1/orders/3')
        self.assertEqual(result.status_code, 200)

    def test_accept_order(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update2))
        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_decline_order(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update))
        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_make_an_order_pending(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update1))
        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_complete_order(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update3))
        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_all_orders_getter(self):
        result = self.client().get('/api/v1/orders')
        self.assertIsNotNone(result)
        self.assertEqual(result.status_code, 200)

    def test_unavailable_fetch(self):
        result1 = self.client().get('/api/v1/orders/222')
        self.assertEqual(result1.status_code, 404)

    def test_invalid_update(self):
        result = self.client().put('/api/v1/orders/344444', content_type='application/json',
                                   data=json.dumps(self.update))
        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)

    def test_invalid_integer_status_id(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update4))
        self.assertEqual(result.status_code, 400)

    def test_non_integer_status_id(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update5))
        self.assertEqual(result.status_code, 400)

    def test_empty_status_id(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update6))
        self.assertEqual(result.status_code, 400)

    def test_menu_getter(self):
        result = self.client().get('/api/v1/menu')
        self.assertEqual(result.status_code, 200)

    def test_users_getter(self):
        result = self.client().get('/api/v1/users')
        self.assertEqual(result.status_code, 200)


    def test_signup(self):

        result = self.client().post('/api/v1/auth/signup', content_type='application/json',
                                   data=json.dumps({
            "first_name": "w ",
            "last_name": " w",
            "address": "j ",
            "residence": "5678",
            "contact": "mmm",
            "email": "bbb",
            "password": "mmmmmm",
            "confirm_password": "mmmmmm",
            "admin_key": 99001122
        }))
        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)