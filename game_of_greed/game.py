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
            self.start_game()
        else:
            self.decline_game()

    def game_round(self):
        self.round_ +=1
        print(f"Starting round {self.round_}")
        print(f"Rolling 6 dice...")
        roll = self._roller(6)
        self.print_dice(roll)
        print("Enter dice to keep, or (q)uit:")
        user_input = input("> ")
        if user_input == "q":
            self.user_quit()
            return
        score = GameLogic.calculate_score(roll)
        print(f"You have {score} unbanked points and 5 dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_input = input("> ")
        if user_input == "q":
            self.user_quit()
            return
        if user_input == "b":
            print(f"You banked {self.banker.shelf(score)} points in round {self.round_}")
            print(f"Total score is {self.banker.bank()} points")
            self.game_round()

    def user_quit(self):
        print(f"Thanks for playing. You earned {self.banker.bank()} points")


    def print_dice(self, dice_rolled):
        output = "*** "
        for die in dice_rolled:
            output += f"{die} "
        output+= "***"
        print(output)

    def decline_game(self):
        print("OK. Maybe another time")

    def start_game(self):
        self.round_ = 0
        self.game_round()
        


if __name__ == "__main__":
    game = Game()
    game.play()
