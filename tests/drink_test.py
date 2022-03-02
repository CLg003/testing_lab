import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("red wine", 3.50)
    
    def test_drink_has_name(self):
        self.assertEqual("red wine", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink.price)