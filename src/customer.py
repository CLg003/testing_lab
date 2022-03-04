class Customer:
    def __init__(self, name, wallet, age, drunk):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunk = drunk

    def reduce_wallet(self, amount):
        self.wallet -= amount
