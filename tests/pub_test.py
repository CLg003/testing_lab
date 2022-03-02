import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        # self.drinks = [
        #     {"name": "red wine", "price": 3.50},
        #     {"name": "espresso martini", "price": 5.00},
        #     {"name": "gin and tonic", "price": 2.95}
        # ]
        self.drink1 = Drink("red wine", 2, 3)
        self.drink2 = Drink("espresso martini", 5, 4)
        drinks = [self.drink1, self.drink2]

        self.pub = Pub("The Practising Pony", 100.00, drinks) #this is set new before every single test is run
        self.customer1 = Customer("George", 4.00, 17, 5)
        self.customer2 = Customer("Mary", 65.00, 42, 2)

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

    def test_check_age_fail(self):
        result = self.pub.check_age(self.customer1)
        self.assertEqual(False, result)

    def test_check_age_pass(self):
        result = self.pub.check_age(self.customer2)
        self.assertEqual(True, result)

    def test_find_alcohol_level(self):
        drink_level = self.pub.find_alcohol_level(self.drink1)
        self.assertEqual(3, drink_level)

    def test_increase_drunk_level(self):
        alcohol_level_number = self.pub.find_alcohol_level(self.drink1)
        self.customer1.drunk += alcohol_level_number
        self.assertEqual(8, self.customer1.drunk)
        
    def test_find_drunk_customer_level(self):
        customer_drunk_level = self.customer1.drunk
        self.assertEqual(5, customer_drunk_level)
    
    def test_customer_too_drunk_true(self):
        too_drunk = self.pub.is_too_drunk(self.customer1)
        self.assertEqual(True, too_drunk)
    
    def test_customer_too_drunk_false(self):
        too_drunk = self.pub.is_too_drunk(self.customer2)
        self.assertEqual(False, too_drunk)
    
    
        