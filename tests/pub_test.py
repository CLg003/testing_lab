import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drinks = [
            {"name": "red wine", "price": 3.50},
            {"name": "espresso martini", "price": 5.00},
            {"name": "gin and tonic", "price": 2.95}
        ]
        self.pub = Pub("The Practising Pony", 100.00, self.drinks) #this is set new before every single test is run

    def test_pub_has_name(self):
        self.assertEqual("The Practising Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(self.drinks, self.pub.drinks)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual) # order matter