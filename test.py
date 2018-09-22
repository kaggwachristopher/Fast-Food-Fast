import unittest
from app.models import RecipeOrders
from instance.config import TestingConfig


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()
        self.order={

        }


    def tearDown(self):
        pass

    def test_all_orders_getter(self):
        self.assertEqual(2, 2)


    def test_single_order_getter(self):
        pass

    def test_order_updater(self):
        pass

    def test_place_order(self):
        pass
