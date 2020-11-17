# Game of Greed
Pull Request: https://github.com/Yonatan1P/game-of-greed/pull/2

Contributors: Brendan Welzien, Mark Bell, Will Motchoffo, Yoni Palagashvili

A python app that allows a player to roll dice, collect points, and gamble to beat the computer. 

We brainstormed a plan to begin the project. We worked on the logic for building the dice all together, and then split off into pairs for pair programming to work through the logic of the calculate score method and the Banker class. We came back together afterwords to compare and collaborate. The lab took a combined 3 hours.
## Features
### Game Logic Class:

Roll Dice - rolls 6 dice, and then incrementally less depending on number of dice kept

Calculate score - calculates the score of each dice roll 

### Banker Class:

shelf method - adds the current calculated score to the temporary shelf

bank method - stores the shelved score into the balance when the round ends

clear shelf method - sets the shelf value back to 0 after every roll

## Testing
### Roll Dice
When rolling 1 to 6 dice ensure…

[x]A sequence of correct length is returned

[x]Each item in sequence is an integer with value between 1 and 6

### Calculate Score
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

### Banker

[x]should properly track unbanked points

[x]should properly add unbanked points to total and return the deposited amount

[x]should remove any unbanked points, resetting to zero.

[x]should not affect previously banked point