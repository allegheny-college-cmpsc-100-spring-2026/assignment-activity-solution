import re
import sys
import random
import ActivityTest

from typing import Any
from unittest.mock import patch
from src.main import *

def test_inventory_test_invalid_quantity():
    inventory = {}
    add_item("quince", inventory)
    assert adjust_qty("quince", -10, inventory) == False

def test_inventory_adjust_qty_upward():
    inventory = {}
    add_item("quince", inventory)
    adjust_qty("quince", 10, inventory)
    assert inventory["quince"]["qty"] == 10

def test_inventory_adjust_qty_downward():
    inventory = {}
    add_item("quince", inventory)
    adjust_qty("quince", 10, inventory)
    adjust_qty("quince", -7, inventory)
    assert inventory["quince"]["qty"] == 3

def test_inventory_query_inventory_positive():
    inventory = {}
    add_item("quince", inventory)
    add_item("pear", inventory)
    add_item("avocado", inventory)
    assert query_inventory("avocado", inventory) == True

def test_inventory_query_inventory_negative():
    inventory = {}
    add_item("quince", inventory)
    add_item("pear", inventory)
    add_item("avocado", inventory)
    assert query_inventory("durian", inventory) == False

def test_inventory_add_item():
    inventory = {}
    assert add_item("quince", inventory) == True and query_inventory("quince", inventory) == True

def test_inventory_valid_sale(capsys):
    inventory = {}
    items = [
        {"quince": {"price": 5.99, "qty": 10}},
        {"durian": {"price": 10.99, "qty":3}},
        {"passionfruit": {"price": 15.99, "qty": 2}}
    ]
    for item in items:
        for fruit in item:
            add_item(fruit, inventory)
            adjust_qty(fruit, item[fruit]["qty"], inventory)
            adjust_price(fruit, item[fruit]["price"], inventory)
    calculate_sale("durian", 3, inventory)
    out, err = capsys.readouterr()
    assert out.strip() == "SALE: 3 durian $32.97"

def test_inventory_invalid_sale(capsys):
    inventory = {}
    items = [
        {"quince": {"price": 5.99, "qty": 10}},
        {"durian": {"price": 10.99, "qty":3}},
        {"passionfruit": {"price": 15.99, "qty": 2}}
    ]
    for item in items:
        for fruit in item:
            add_item(fruit, inventory)
            adjust_qty(fruit, item[fruit]["qty"], inventory)
            adjust_price(fruit, item[fruit]["price"], inventory)
    calculate_sale("durian", 10, inventory)
    out, err = capsys.readouterr()
    assert out.strip() == "We can't sell that many!"

def test_inventory_show_all(capsys):
    inventory = {}
    items = [
        {"quince": {"price": 5.99, "qty": 10}},
        {"durian": {"price": 10.99, "qty":3}},
        {"passionfruit": {"price": 15.99, "qty": 2}}
    ]
    for item in items:
        for fruit in item:
            add_item(fruit, inventory)
            adjust_qty(fruit, item[fruit]["qty"], inventory)
            adjust_price(fruit, item[fruit]["price"], inventory)
    show_all(inventory)
    out, err = capsys.readouterr()
    assert out.strip() == "Name\tPrice\tQuantity\nquince\t5.99\t10\ndurian\t10.99\t3\npassionfruit\t15.99\t2"

def test_inventory_show_one(capsys):
    inventory = {}
    add_item("quince", inventory)
    adjust_qty("quince", 12, inventory)
    adjust_price("quince", 15, inventory)
    show_all(inventory)
    out, err = capsys.readouterr()
    assert out.strip() == "Name\tPrice\tQuantity\nquince\t15\t12"

def test_main_inventory_all_operations(capsys):
    inventory = {}
    outputs = []
    with patch(
         "builtins.input", 
         side_effects = [
              "y"
         ]
    ):
        add_item("quince", inventory)
        inventory["quince"]["price"] = 10.00
        adjust_qty("quince", 5, inventory)
        show_all({"quince": inventory["quince"]})
        show_all(inventory)
    out, err = capsys.readouterr()
    err = None if err == '' else Any
    assert err == None
        

def test_main_inventory_system_menu_and_exit(capsys):
    with patch(
           "builtins.input", 
        side_effect = [
                "1", "quince", "y",
                "2", "quince", "5.99", 
                "3", "quince", "10", 
                "4", "quince",
                "5",
                "6", "quince", "7",
                "e"
            ]
        ):
            main()
    out, err = capsys.readouterr()
    err = None if err == '' else Any
    assert err == None