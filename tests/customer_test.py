import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("red wine", 2)
        self.drink2 = Drink("espresso martini", 5)
        drinks = [self.drink1, self.drink2]

        self.customer = Customer("Szymon", 200.00, 21)
        self.pub = Pub("Anything", 300, drinks)

    def test_customer_has_name(self):
        self.assertEqual("Szymon", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(200, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.50)
        self.assertEqual(196.50, self.customer.wallet)

    def test_customer_buy_drink(self):
        self.customer.buy_drink("espresso martini", self.pub)
        self.assertEqual(195, self.customer.wallet)
        self.assertEqual(305, self.pub.till)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)
        
