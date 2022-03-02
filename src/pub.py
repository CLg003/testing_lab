class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks
        self.breaking_drunk_point = 3

    def increase_till(self, amount):
        self.till += amount

    def find_drink_price(self, drink_name):
        for drink in self.drinks:
            if drink_name == drink.name:
                return drink.price
    
    def check_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def find_alcohol_level(self, drink):
        return drink.alcohol_level

    def increase_drunk_level(self, customer, drink):
        alcohol_level = self.find_alcohol_level(drink)
        customer.drunk += alcohol_level

    def find_drunk_customer_level(self, customer):
        return customer.drunk

    def check_drunk_level(self, customer):
        if customer.drunk < 10:
            return True
        return False

