import re
import sys
import random
import ActivityTest

from unittest.mock import patch

from src.main import *


def test_normalize_move():
    moves = [1, 2, 3, 4, 5]
    for move in moves:
        result = normalize_move(move)
        assert result in VALID_MOVES


def test_normalize_invalid_move():
    result = normalize_move(7)
    assert result == "invalid"


def test_player_wins():
    wins = {
        "rock": ("scissors", "lizard"),
        "paper": ("rock", "spock"),
        "scissors": ("paper", "lizard"),
        "lizard": ("spock", "paper"),
        "spock": ("scissors", "rock"),
    }
    for win in wins:
        player = win
        for loss in wins[win]:
            assert "player" == decide_winner(player, loss)


def test_computer_wins():
    wins = {
        "rock": ("scissors", "lizard"),
        "paper": ("rock", "spock"),
        "scissors": ("paper", "lizard"),
        "lizard": ("spock", "paper"),
        "spock": ("scissors", "rock"),
    }
    for win in wins:
        computer = win
        for loss in wins[win]:
            assert "computer" == decide_winner(loss, computer)


def test_ties():
    for move in VALID_MOVES:
        assert "tie" == decide_winner(move, move)


def test_menu_round(capsys):
    with patch("builtins.input", side_effect=[1, 6]):
        main()


def test_menu_round_invalid_move(capsys):
    with patch("builtins.input", side_effect=[7, 6]):
        main()
