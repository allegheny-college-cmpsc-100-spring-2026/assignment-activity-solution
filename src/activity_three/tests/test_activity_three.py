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

def test_generate_for_type(capsys):
    seed = generate(low = 100, high = 100)

def test_make_progressive_low(capsys):
    answer = random.randint(1, 50)
    guess = random.randint(51, 100)
    assert make_progressive(answer = answer, guess = guess) < guess

def test_make_progressive_high(capsys):
    answer = random.randint(51, 100)
    guess = random.randint(1, 50)
    assert make_progressive(answer = answer, guess = guess) > guess

def test_play_game_for_win(capsys):
    with patch("builtins.input", side_effect = ["85", "n"]):
        main(answer = 85)
    out, err = capsys.readouterr()
    assert 'You were right on!' in out.split("\n")
    assert 'It took you 1 guess(es)' in out.split("\n")