import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    
    def setUp(self):
        # self.drinks = [
        #     {"name": "red wine", "price": 3.50},
        #     {"name": "espresso martini", "price": 5.00},
        #     {"name": "gin and tonic", "price": 2.95}
        # ]
        self.drink1 = Drink("red wine", 2)
        self.drink2 = Drink("espresso martini", 5)
        drinks = [self.drink1, self.drink2]

        self.pub = Pub("The Practising Pony", 100.00, drinks) #this is set new before every single test is run

    def test_pub_has_name(self):
        self.assertEqual("The Practising Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual([self.drink1, self.drink2], self.pub.drinks)

    def test_find_drink_price(self):
        price = self.pub.find_drink_price("espresso martini")
        self.assertEqual(5, price)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual) # order matter