from Book import Book
from Library import Library
from time import sleep

def menu() -> str:
    return """\033c1. Add a book
2. Search library by title
3. Remove a book
4. Display books
5. Quit
"""

def main() -> None:
    lib = Library()
    while True:
        
        print(menu())
        choice = int(input("Choose an option: "))
        match choice:

            case 1:
                title = input("Title: ")
                author = input("Author: ")
                pages = int(input("Page Count: "))
                entry = Book(title = title, author = author, pages = pages)
                lib.add_book(entry)
            
            case 2:
                request = input("Enter title to search: ")
                book = lib.search(query = request)
                print(f"Found: {book}")
            
            case 3:
                title = input("Input title to remove: ")
                lib.remove_book(title = title)
            
            case 4:
                lib.display()
            
            case 5 | _:
                break
        
        sleep(1)

if __name__ == "__main__":
    main()