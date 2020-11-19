import random
from collections import Counter


class GameLogic:

    @staticmethod
    def calculate_score(dice_roll):
        score = 0
        dice = Counter(dice_roll)
        # scoring for a straight or three sets of pairs
        if len(dice) == 6 or (len(dice) == 3 and dice.most_common()[2][1] == 2):
            return 1500
        sets = dice.most_common()
        if len(sets) and sets[0][1] >= 3:
            score += GameLogic.score_for_set(sets[0][0], sets[0][1])
        if len(sets) > 1 and sets[1][1] >= 3:
            score += GameLogic.score_for_set(sets[1][0], sets[1][1])
        if dice[1] <= 2:
            score += dice[1] * 100
        if dice[5] <= 2:
            score += dice[5] * 50
        return score

    @staticmethod
    def score_for_set(num_of_dimples, num_of_dice):
        score = num_of_dimples * 100 * (num_of_dice - 2)
        if num_of_dimples == 1:
            score *= 10
        return score

    @staticmethod
    def roll_dice(number):
        all_dice = []
        while number:
            random_number = random.randint(1, 6)
            all_dice.append(random_number)
            number = number-1
        return all_dice

    @staticmethod
    def get_scorers(dice):
        include_score = GameLogic.calculate_score(dice)
        scorers = []
        for die in dice:
            test_dice = list(dice)
            test_dice.remove(die)
            exclude_score = GameLogic.calculate_score(test_dice)
            if include_score != exclude_score:
                scorers.append(die)
        return tuple(scorers)

    @staticmethod
    def validate_keepers(dice_rolled, requested_keepers):
        roll = Counter(dice_rolled)
        keepers = Counter(requested_keepers)
        for keeper in keepers:
            if keepers[keeper] > roll[keeper]:
                return False
        return True
