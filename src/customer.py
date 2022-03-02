
class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_wallet(self, amount):
        self.wallet -= amount

    # write buy_drink()
    def buy_drink(self, drink_name, pub):
        drink_price = pub.find_drink_price(drink_name)
        self.reduce_wallet(drink_price)
        pub.increase_till(drink_price)