class Banker:

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, shelved=0):
        self.shelved += shelved
        return self.shelved

    def bank(self):
        self.balance += self.shelved
        self.clear_shelf()
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved
