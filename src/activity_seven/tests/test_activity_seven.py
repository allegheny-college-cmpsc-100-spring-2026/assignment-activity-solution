import re
import sys
import random
import ActivityTest

from typing import Any
from unittest.mock import patch

from src.main import *
from src.Book import *
from src.Library import *

def test_create_library():
    lib = Library()
    assert type(lib) == Library

def test_create_book():
    book = Book(
        title = "That This",
        author = "Susan Howe",
        pages = 112
    )
    assert type(book) == Book

def test_add_book():
    lib = Library()
    book = Book(
        title = "That This",
        author = "Susan Howe",
        pages = 112
    )
    lib.add_book(book = book)
    assert len(lib.books) == 1

def test_remove_book():
    lib = Library()
    book = Book(
        title = "That This",
        author = "Susan Howe",
        pages = 112
    )
    lib.add_book(book = book)
    lib.remove_book(title = "That This")
    assert len(lib.books) == 0

def test_remove_book_complex():
    lib = Library()
    book_one = Book(
        title = "That This",
        author = "Susan Howe",
        pages = 112
    )
    lib.add_book(book = book_one)
    book_two = Book(
        title = "Moby Dick",
        author = "Herman Melville",
        pages = 750
    )
    lib.add_book(book = book_two)
    lib.remove_book(title = "Moby Dick")
    assert len(lib.books) == 1

def test_search_book():
    lib = Library()
    book = Book(
        title = "That This",
        author = "Susan Howe",
        pages = 112
    )
    lib.add_book(book = book)
    result = lib.search(query = "That This")
    assert result == book

def test_display_books(capsys):
    lib = Library()
    book = Book(
        title = "That This",
        author = "Susan Howe",
        pages = 112
    )
    lib.add_book(book = book)
    lib.display()
    out, err = capsys.readouterr()
    assert out.strip() == "Title\tAuthor\tPage Count\nThat This\tSusan Howe\t112"

def test_use_all_menu_functions(capsys):
    with patch(
           "builtins.input", 
        side_effect = [
                "1", "That This", "Susan Howe", "112",
                "2", "That This",
                "3", "That This",
                "4",
                "5"
            ]
        ):
            main()
    out, err = capsys.readouterr()
    err = None if err == '' else Any
    assert err == None