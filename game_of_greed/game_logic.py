import random
from collections import Counter

class GameLogic:

    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        dice = Counter(dice_roll)
        # scoring for a straight or three sets of pairs
        if len(dice) == 6 or (len(dice) == 3 and dice[3] == 2):
            return 1500
        sets = dice.most_common()
        if len(sets) and sets[0][1] >= 3:
            score+= GameLogic.score_for_set(sets[0][0], sets[0][1])
        if len(sets) > 1 and sets[1][1] >= 3:
            score+= GameLogic.score_for_set(sets[1][0], sets[1][1])
        if dice[1] <= 2:
            score += dice[1] * 100
        if dice[5] <= 2:
            score += dice[5] * 50
        return score


    @staticmethod
    def score_for_set(num_of_dimples, num_of_dice):
        score = num_of_dimples * 100 *(num_of_dice - 2)
        if num_of_dimples == 1:   
            score *= 10
        return score

    @staticmethod
    def roll_dice(number):
        all_dice = []
        while number:
            random_number=random.randint(1,6)
            all_dice.append(random_number)
            number = number-1
        return all_dice
