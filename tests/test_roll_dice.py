import pytest 
from game_of_greed.game_logic import GameLogic

def test_roll_dice():
    actual = len(roll_dice(6))
    expected = 6
    assert actual == expected