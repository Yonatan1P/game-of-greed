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

    def shelf(self):
        pass

    def bank(self):
        pass

    def clear_shelf(self):
        pass
