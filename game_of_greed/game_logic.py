import random
from collections import Counter

class GameLogic:

    def calculate_score(self):
        pass

    @staticmethod
    def roll_dice(number):
        all_dice = []
        while number:
            random_number=random.randint(1,6)
            all_dice.append(random_number)
            number = number-1
        return all_dice

class Banker:

    def __init__(self):
        self.balance = 0
        self.shelved = 0

    def shelf(self, shelved):
        self.shelved += shelved
        return self.shelved

    def bank(self):
        self.balance += self.shelved
        self.clear_shelf()
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
        return self.shelved
       