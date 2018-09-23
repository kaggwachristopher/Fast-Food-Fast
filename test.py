import unittest
from app.app import app
from flask import json


class Testing(unittest.TestCase):

    def setUp(self):
        self.api = app
        self.client = self.api.test_client
        self.order = {
            "order_date": "2018-09-22 02:36:27.956913",
            "order_id": 3,
            "order_status": "Pending",
            "quantity": "5",
            "recipe_id": "4",
            "user_id": "21"
        }
        self.update = {
            "status_id": 2
        }
        self.update1 = {
            "status_id": 7
        }

    def tearDown(self):
        pass

    def test_all_orders_getter(self):
        result = self.client().get('/api/v1/orders')
        self.assertEqual(result.status_code, 200)

    def test_single_order_getter(self):
        result = self.client().get('/api/v1/orders/3')
        self.assertEqual(result.status_code, 200)

    def test_unavailable_fetch(self):
        result1 = self.client().get('/api/v1/orders/222')
        self.assertEqual(result1.status_code, 404)

    def test_order_updater(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update))
        self.assertEqual(result.status_code, 201)
        self.assertIsNotNone(result)

    def test_invalid_update(self):
        result = self.client().put('/api/v1/orders/4', content_type='application/json',
                                   data=json.dumps(self.update))
        self.assertEqual(result.status_code, 404)
        self.assertIsNotNone(result)

    def test_invalid_status_id(self):
        result = self.client().put('/api/v1/orders/3', content_type='application/json',
                                   data=json.dumps(self.update1))
        self.assertEqual(result.status_code, 403)

    def test_place_order(self):
        result = self.client().post('/api/v1/orders', content_type='application/json',
                                    data=json.dumps(self.order))
        self.assertEqual(result.status_code, 201)
