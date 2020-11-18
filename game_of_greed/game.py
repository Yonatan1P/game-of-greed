from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
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
        self.round_ += 1
        print(f"Starting round {self.round_}")
        self.game_round_rolling_phase(6)

    def game_round_rolling_phase(self, num_of_dice):
        print(f"Rolling {num_of_dice} dice...")
        roll = self._roller(num_of_dice)
        self.print_dice(roll)
        self.game_round_keep_phase(num_of_dice, roll)

    def game_round_keep_phase(self, num_of_dice, roll):
        kept_dice = None
        while not kept_dice:
            print("Enter dice to keep, or (q)uit:")
            user_input = input("> ")
            if user_input == "q":
                self.user_quit()
                return
            kept_dice = self.validate_dice(roll, user_input)
        # TODO, we should not pass the roll, but instead pass the kept dice
        # once that function is built
        self.game_round_gambling_phase(num_of_dice-len(kept_dice), roll)

    def game_round_gambling_phase(self, num_of_dice, kept_dice):
        score = GameLogic.calculate_score(kept_dice)
        print(f"You have {score} unbanked points and {num_of_dice} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_input = input("> ")
        if user_input == "q":
            self.user_quit()
            return
            
        if user_input == "b":
            print(f"You banked {self.banker.shelf(score)} points in round {self.round_}")
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
        print(f"Thanks for playing. You earned {self.banker.bank()} points")

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