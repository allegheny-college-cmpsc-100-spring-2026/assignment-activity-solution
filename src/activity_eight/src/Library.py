import json
import pickle

from os.path import exists
from Patron import Patron
from Book import Fiction, Poetry, Nonfiction

class Library:

    def __init__(self):
        # Load the catalog data
        with open("src/data/books.json", "r") as fh:
            self.catalog = json.load(fh)
        self.__categorize_books()
        
        # Load current patron data
        if exists("src/data/tracking.pickle"):
            with open("src/data/tracking.pickle", "rb") as fh:
                self.books = pickle.load(fh)

    def __categorize_books(self):
        self.books = []
        for book in self.catalog:
            match book["genre"]:
                case "Fiction":
                    b = Fiction(
                        title = book["title"], 
                        author = book["author"], 
                        pages = book["page_count"]
                    )
                case "Poetry":
                    b = Poetry(
                        title = book["title"], 
                        author = book["author"], 
                        pages = book["page_count"]
                    )
                case "Nonfiction":
                    b = Nonfiction(
                        title = book["title"],
                        author = book["author"],
                        pages = book["page_count"],
                        subject = book["subject"]
                    )
            self.books.append(b)
    
    def checkout(self, book: Fiction | Nonfiction | Poetry, patron: Patron):
        book.checkout_to(patron)
        with open("src/data/tracking.pickle", "wb") as fh:
            pickle.dump(self.books, fh)

    def display(self):
        for book in self.books:
            print(book.__dict__)
            
