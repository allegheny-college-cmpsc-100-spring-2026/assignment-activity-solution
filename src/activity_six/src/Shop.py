from pathlib import Path

class Inventory:

    MODULE_PATH = Path(__file__).parent.resolve()

    @staticmethod
    def menu():
        print("\033c", end="")
        print("""
Fruit Stand Inventory 1.0              

1. Add item
2. Price item
3. Adjust quantity
4. Check item
5. List inventory
6. Sell an item
        """)