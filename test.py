import unittest
from app.models import RecipeOrders
from app import Environment
from instance.config import TestingConfig

env = Environment()

class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = env.create_app(TestingConfig)
        self.order = {
                        "order_date": "2018-09-22 02:36:27.956913",
                        "order_id": 3,
                        "order_status": "Pending",
                        "quantity": "5",
                        "recipe_id": "4",
                        "user_id": "21"
                     }


    # def tearDown(self):
    #     pass

    def test_all_orders_getter(self):
        self.assertEqual(2, 2)


    # def test_single_order_getter(self):
    #     pass
    #
    # def test_order_updater(self):
    #     pass
    #
    # def test_place_order(self):
    #     pass
