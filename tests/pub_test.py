import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("red wine", 2, 3)
        self.drink2 = Drink("espresso martini", 5, 4)
        drinks = [self.drink1, self.drink2]

        self.pub = Pub("The Practising Pony", 100.00, drinks) #this is set new before every single test is run
        self.customer1 = Customer("George", 4.00, 17, 5)
        self.customer2 = Customer("Mary", 65.00, 42, 9)
        self.customer_young = Customer("Claire", 10, 15, 7)
        self.customer_drunk = Customer("Andy", 32.50, 37, 11)

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
        self.assertEqual(expected, actual)

    def test_customer_reduce_wallet(self):
        self.customer2.reduce_wallet(self.pub.find_drink_price("espresso martini"))
        self.assertEqual(60, self.customer2.wallet)

    # @unittest.skip("delete this line to run the test")
    def test_sell_drink_customer_old(self):
        self.pub.sell_drink("espresso martini", self.customer2)
        self.assertEqual(5, self.pub.find_drink_price("espresso martini"))
        self.assertEqual(60, self.customer2.wallet)
        self.assertEqual(105, self.pub.till)

    # @unittest.skip("delete this line to run the test")
    def test_sell_drink_customer_young(self):
        self.pub.sell_drink("espresso martini", self.customer_young)
        self.assertEqual(10, self.customer_young.wallet)
        self.assertEqual(100, self.pub.till)

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

    def test_check_drunk_level_can_serve(self):
        result = self.pub.check_drunk_level(self.customer1)
        self.assertEqual(True, result)

    def test_check_drunk_level_do_not_serve(self):
        result = self.pub.check_drunk_level(self.customer_drunk)
        self.assertEqual(False, result)
        
    # @unittest.skip("delete this line to run the test")
    def test_customer_buy_drink_drunk_level_okay(self):
        self.pub.sell_drink("red wine", self.customer2)
        self.assertEqual(63, self.customer2.wallet)
        self.assertEqual(102, self.pub.till)
    
    # @unittest.skip("delete this line to run the test")
    def test_customer_buy_drink_drunk_level_too_high(self):
        self.pub.sell_drink("red wine", self.customer_drunk)
        self.assertEqual(32.50, self.customer_drunk.wallet)
        self.assertEqual(100, self.pub.till)

    def test_can_add_drinks_to_empty_stock(self):
        self.pub.add_drinks_to_stock(self.pub.drinks)
        expected = {self.drink1: 1, self.drink2: 1}
        self.assertEqual(expected, self.pub.stock)

    def test_can_increase_level_of_stock(self):
        self.pub.add_drinks_to_stock(self.pub.drinks)
        self.pub.add_drinks_to_stock(self.pub.drinks)
        expected = {self.drink1: 2, self.drink2: 2}
        self.assertEqual(expected, self.pub.stock)