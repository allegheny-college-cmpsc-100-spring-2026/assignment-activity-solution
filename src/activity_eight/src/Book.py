from datetime import datetime, timedelta
from Patron import Patron

class Book:

    def __init__(self, title: str = "", author: str = "", pages: int = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.patron = None
        self.due_date = None

    def __str__(self):
        return(f"""{self.title}
{self.author}
{self.pages}
{self.genre}
Checkout out by: {self.patron.name}
Due back by: {self.due_date}
""")
    
    def checkout_to(self, patron: Patron):
        if not self.patron:
            patron.checked_out.append(self)
            self.due_date = datetime.now() + timedelta(days = 7)
            self.patron = patron
        else:
            print("Already checked out!")

class Poetry(Book):
    
    def __init__(self, title: str = "", author: str = "", pages: int = 0):
        super().__init__(title = title, author = author, pages = pages)
        self.genre = "Poetry"

class Fiction(Book):

    def __init__(self, title: str = "", author: str = "", pages: int = 0):
        super().__init__(title = title, author = author, pages = pages)
        self.genre = "Fiction"

class Nonfiction(Book):
    def __init__(self, title: str = "", author: str = "", pages: int = 0, subject: str = ""):
        super().__init__(title = title, author = author, pages = pages)
        self.subject = subject
    
    def __str__(self):
        return(f"""{self.title}
{self.author}
{self.pages}
{self.subject}
Checked out by: {self.patron.name}
Due back by: {self.due_date}
""")
