import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Szymon", 200.00)

    def test_customer_has_name(self):
        self.assertEqual("Szymon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(200, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.50)
        self.assertEqual(196.50, self.customer.wallet)
