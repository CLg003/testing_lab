class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def find_drink_price(self, drink_name):
        for drink in self.drinks:
            if drink_name == drink.name:
                return drink.price