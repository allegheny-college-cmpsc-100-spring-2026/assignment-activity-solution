import re
import sys
import random
import ActivityTest

from unittest.mock import patch
from src import WordList
from src.main import *

def test_main_exec_no_err(capsys):
    words = List.load()
    with patch("builtins.input", side_effect = ["0"]):
        main(words)
    out, err = capsys.readouterr()
    assert err == ''

def test_main_limit_zero(capsys):
    words = List.load()
    with patch("builtins.input", side_effect = ["0"]):
        main(words)
    out, err = capsys.readouterr()
    out = out.split("\n")
    assert len(out) - 1 == 17850

def test_main_count_output_dbl(capsys):
    words = List.load()
    with patch("builtins.input", side_effect = ["1"]):
        main(words)
    out, err = capsys.readouterr()
    out = out.split("\n")
    assert len(out) - 1 == 4591

def test_main_count_output_dbl_dbl(capsys):
    words = List.load()
    with patch("builtins.input", side_effect = ["2"]):
        main(words)
    out, err = capsys.readouterr()
    out = out.split("\n")
    assert len(out) - 1 == 241

def test_main_count_output_triple_dbl(capsys):
    words = List.load()
    with patch("builtins.input", side_effect = ["3"]):
        main(words)
    out, err = capsys.readouterr()
    out = out.split("\n")
    assert len(out) - 1 == 19

def test_main_count_output_quad_dbl(capsys):
    words = List.load()
    with patch("builtins.input", side_effect = ["4"]):
        main(words)
    out, err = capsys.readouterr()
    out = out.split("\n")
    assert len(out) - 1 == 0