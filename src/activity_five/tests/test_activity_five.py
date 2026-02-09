import re
import sys
import random
import ActivityTest

from unittest.mock import patch
from src.machine import Pin
from src.main import *

def test_signal_output_short():
    btn = Pin(None, Pin.OUT, value = ["short"])
    btn.val == 0
    assert press(btn) == "short"

def test_signal_output_long():
    btn = Pin(None, Pin.OUT, value = ["long"])
    btn.val == 0
    assert press(btn) == "long"

def test_reset_list():
    assert reset_instruction() == []

def test_swap_selected_values():
    values = [1, 10, 5, 9, 20, 2, 33]
    instruction = [2, 4]
    assert select(
        values = values, 
        choice = instruction
    ) == [
        1, 9, 5, 10, 20, 2, 33
    ]

def test_mock_longer_problem():
    values = [1, 10, 5, 9, 20, 2, 33]
    instructions = [
        [2,6],
        [5,6]
    ]
    for inst in instructions:
        values = select(values, inst)
    assert values == [1, 2, 5, 9, 10, 20, 33]

def test_mock_framework_presses(capsys):
    main([3,4,2,1])
    out, err = capsys.readouterr()
    out = eval(list(out.split("\n"))[-2])
    assert out == [1, 2, 3, 4]