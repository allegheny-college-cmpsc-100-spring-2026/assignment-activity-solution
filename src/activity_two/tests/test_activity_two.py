import re
import sys
import ActivityTest

from unittest.mock import patch
from src.main import *

def test_main_exec_no_err(capsys):
    with patch("builtins.input", side_effect = ["1-100"]):
        main()
    out, err = capsys.readouterr()
    assert err == ''

def test_main_exec_hello_output(capsys):
    with patch("builtins.input", side_effect = ["1-100"]):
        main()
    out, err = capsys.readouterr()
    assert re.search(
        re.compile("^((?!world)[\\s\\S])*$"), 
        out
    )

def test_main_exec_calculate_spread_output(capsys):
    with patch("builtins.input", side_effect = ["2-4024"]):
        main()
    out, err = capsys.readouterr()
    match = re.search(
        re.compile("Calculating [0-9]+\\-[0-9]+"), 
        out
    )
    assert match.group() == "Calculating 2-4024"

def test_main_exec_compute_output(capsys):
    with patch("builtins.input", side_effect = ["1-100"]):
        main()
    out, err = capsys.readouterr()
    assert re.search(
        re.compile("5050"), 
        out
    )