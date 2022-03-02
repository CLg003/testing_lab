
class Customer:
    def __init__(self, name, wallet, age, drunk):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunk = drunk

    def reduce_wallet(self, amount):
        self.wallet -= amount

    # write buy_drink()
    def buy_drink(self, drink_name, pub):
        if pub.check_age(self):
            drink_price = pub.find_drink_price(drink_name)
            self.reduce_wallet(drink_price)
            pub.increase_till(drink_price)
        