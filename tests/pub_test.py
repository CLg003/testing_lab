import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Practising Pony", 100.00) #this is set new before every single test is run

    def test_pub_has_name(self):
        self.assertEqual("The Practising Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual) # order matter