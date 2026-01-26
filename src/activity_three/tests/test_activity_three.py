import re
import sys
import random
import ActivityTest

from unittest.mock import patch
from src.main import *

def test_main_exec_no_err(capsys):
    with patch("builtins.input", side_effect = ["1", "n"]):
        main()
    out, err = capsys.readouterr()
    assert err == ''

def test_message_with_statuses(capsys):
    statuses = ["too high", "too low", "right on"]
    for status in statuses:
        assert message(status) == f"You were {status}!"

def test_evaluate_for_type(capsys):
    guess = random.randint(1,100)
    assert type(evaluate(guess)) == bool

def test_play_game_until_win(capsys):
    numbers = list(range(1,101))
    for number in numbers:
        if evaluate(number):
            break
    assert evaluate(number) == True