# Game of Greed
Day 1 Pull Request: https://github.com/Yonatan1P/game-of-greed/pull/2

Day 2 Pull Request: https://github.com/Yonatan1P/game-of-greed/pull/4

Contributors: Brendan Welzien, Mark Bell, Will Motchoffo, Yoni Palagashvili

A python app that allows a player to roll dice, collect points, and gamble to beat the computer. 

We brainstormed a plan to begin the project. We worked on the logic for building the dice all together, and then split off into pairs for pair programming to work through the logic of the calculate score method and the Banker class. We came back together afterwords to compare and collaborate. The lab took a combined 3 hours.
## Day 1 (Version 1)
Monday-11/16/2020
Lab06
### Features
#### Game Logic Class:

Roll Dice - rolls 6 dice, and then incrementally less depending on number of dice kept

Calculate score - calculates the score of each dice roll 

#### Banker Class:

shelf method - adds the current calculated score to the temporary shelf

bank method - stores the shelved score into the balance when the round ends

clear shelf method - sets the shelf value back to 0 after every roll

### Testing
#### Roll Dice
When rolling 1 to 6 dice ensure…

[x]A sequence of correct length is returned

[x]Each item in sequence is an integer with value between 1 and 6

#### Calculate Score
[x]zilch - non scoring roll should return 0

[x]ones - rolls with various number of 1s should return correct score

[x]twos - rolls with various number of 2s should return correct score

[x]threes - rolls with various number of 3s should return correct score

[x]fours - rolls with various number of 4s should return correct score

[x] fives - rolls with various number of 5s should return correct score

[x] sixes - rolls with various number of 6s should return correct score

[x]straight - 1,2,3,4,5,6 should return correct score

[x]three_pairs - 3 pairs should return correct score

[x]two_trios - 2 sets of 3 should return correct score

[x]leftover_ones - 1s not used in set of 3 (or greater) should return correct score

[x]leftover_fives - 5s not used in set of 3 (or greater) should return correct score

#### Banker

[x]should properly track unbanked points

[x]should properly add unbanked points to total and return the deposited amount

[x]should remove any unbanked points, resetting to zero.

[x]should not affect previously banked point

## Day 2 (Version 2)
Tuesday 11/17/2020

Lab07

Game Simulation

We all worked as a group for this entire lab. The provided unit tests gave us a direction for coding, and we used the provided txt files to outline how our code should interact with the user. This, in conjuction with our previously built GameLogic, we were able to piece together a function that could handle our unit tests. Then we spent some time refactoring to make the code more modular and easier to read and debug. 

Logic Done in game_of_greed.game.py
### Features
Prompt user with option to start new game or quit
#### Roll Dice
Defined in the game_round_rolling_phase
Roll dice when user starts new round
Uses roll_dice function from GameLogic to generate the given number of dice
The rolled dice are passed on to the keep phase
#### Keep Dice
Defined in the game_round_keep_phase

From the given roll, users are prompted to input the numbers they want to keep

TODO: We still need to validate that the user's input is valid based on the rules of scoring.

The kept dice are passed on to the banking phase
#### Banking
Defined in the game_round_gambling_phase

For a given set of kept dice, we use the calculate_score function from GameLogic to calculate the score of the given kept dice combination.

The user is informed of the number of points they have shelved, and the number of di remaining for rerolling 
#### Rounds
This is handled between the gambling phase and the new round. 

If a user chooses to bank their points, then the next round starts automatically.

Every time a new round starts, the start_new_round method increments the round.
### Testing
Found in tests.version_2

all tests passing in test_sim_basic.py

mirroring the 4 sim.txt files provided:

- [x] bank_first_for_two_rounds

- [x] bank_one_roll_then_quit

- [x] one_and_done

- [x] quitter

