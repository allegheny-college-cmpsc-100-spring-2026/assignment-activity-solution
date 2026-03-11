class Book:

    title: str
    author: str
    year: int

    def __init__(self, title: str = "", author: str = "", pages: int = 0):
        self.title = title
        self.author = author
        self.page_count = pages

    def __str__(self) -> str:
        return f"{self.title}\t{self.author}\t{self.page_count}"