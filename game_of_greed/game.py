from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.dice_remaining = None
        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_ = 0
        self._roller = None

    def play(self, roller=None):
        """Entry point for playing (or declining) a game

        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self.round_num = 0

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_new_round()
        else:
            self.decline_game()

    def start_new_round(self):
        if self.round_ > self.num_rounds:
            self.user_quit()
            return
        self.round_ += 1
        print(f"Starting round {self.round_}")
        self.dice_remaining = 6
        self.game_round_rolling_phase()

    def game_round_rolling_phase(self):
        if not self.dice_remaining:
            self.dice_remaining = 6
        print(f"Rolling {self.dice_remaining} dice...")
        roll = self._roller(self.dice_remaining)
        self.game_round_keep_phase(roll)

    def game_round_keep_phase(self, roll):
        self.print_dice(roll)
        if not GameLogic.calculate_score(roll):
            print('****************************************\n'
                  '**        Zilch!!! Round over         **\n'
                  '****************************************')
            print(f"You banked {self.banker.balance} points in round {self.round_}")
            print(f"Total score is {self.banker.balance} points")
            self.banker.clear_shelf()
            self.start_new_round()
            return
        kept_dice = None
        user_input = None
        while not user_input:
            print("Enter dice to keep, or (q)uit:")
            user_input = input("> ")
            if user_input == "q":
                self.user_quit()
                return
        parsed_input = [int(number) for number in user_input if number.isnumeric()]
        if not GameLogic.validate_keepers(roll, parsed_input):
            print('Cheater!!! Or possibly made a typo...')
            self.game_round_keep_phase(roll)
            return
        kept_dice = GameLogic.get_scorers(roll)
        # TODO, we should not pass the roll, but instead pass the kept dice
        # once that function is built
        self.dice_remaining -= len(kept_dice)
        self.game_round_gambling_phase(roll)

    def game_round_gambling_phase(self, kept_dice):
        score = GameLogic.calculate_score(kept_dice)
        self.banker.shelf(score)
        print(f"You have {self.banker.shelved} unbanked points and {self.dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_input = input("> ")
        if user_input == "r":
            self.game_round_rolling_phase()
            return
        if user_input == "q":
            self.user_quit()
            return
            
        if user_input == "b":
            print(f"You banked {self.banker.shelved} points in round {self.round_}")
            print(f"Total score is {self.banker.bank()} points")
            self.start_new_round()
            return

    # TODO: this function should return a list or tuple of dice that the user is keeping
    # it should not allow the user to keep dice that dont exist, or dice that that cannot score
    def validate_dice(self, roll, user_input):
        wants_to_keep = []
        for char in user_input:
            wants_to_keep += char
        return wants_to_keep

    def user_quit(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")

    def print_dice(self, dice_rolled):
        output = "*** "
        for die in dice_rolled:
            output += f"{die} "
        output += "***"
        print(output)

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):
        self.round_ = 0
        self.start_new_round()      


if __name__ == "__main__":
    game = Game()
    game.play()