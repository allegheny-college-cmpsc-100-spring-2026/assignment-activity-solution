import json

from Book import Book

class Library:

    books: list[Book]

    def __init__(self):
        self.books = []
    
    def __str__(self) -> str:
        return f"This library contains {len(self.books)} books."
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def remove_book(self, title: str = ""):
        book = self.search(query = title)
        if book:
            idx = self.books.index(book)
            self.books.pop(idx)

    def search(self, query: str = "") -> Book:
        for entry in self.books:
            if entry.title == query:
                return entry

    def display(self) -> None:
        print("Title\tAuthor\tPage Count")
        for book in self.books:
            print(book)