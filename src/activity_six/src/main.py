from time import sleep
from Shop import Inventory

def query_inventory(name: str = "", on_hand: dict = {}) -> bool:
    """
    Docstring for query_inventory

    :param name: Name of an item
    :type name: str
    :param on_hand: Quantity held
    :type on_hand: dict
    :return: Status of item held in on_hand
    :rtype: bool
    """
    if name in on_hand:
        return True
    return False

def add_item(name: str = "", on_hand: dict = {}) -> bool:
    """
    Adds an item to inventory if it doesn't exist already.

    :param name: Name of an item
    :type name: str
    :param on_hand: Quantity held
    :type on_hand: dict
    :return: Description
    :rtype: bool
    """
    # Look up item (e.g., apples) in on_hand
    if not query_inventory(name = name, on_hand = on_hand):
        on_hand[name] = {"price": 0, "qty": 0}
        return True
    return False

def check_item(name: str = "", on_hand: dict = {}) -> None:
    """
    Check if item exists; if not, prompt user to verify

    :param name: Name of item
    :type name: str
    :param on_hand: Quantity held
    :type on_hand: dict
    """
    if not query_inventory(name = name, on_hand = on_hand):
        response = input(f"Add {name} to inventory (Y/N)? ").lower()
        if response == "y":
            add_item(name = name, on_hand = on_hand)

def adjust_qty(name: str = "", qty: int = 0, on_hand: dict = {}) -> bool:
    """
    Docstring for adjust_qty

    :param name: Description
    :type name: str
    :param qty: Description
    :type qty: int
    :param inventory: Description
    :type inventory: dict
    :return: Description
    :rtype: bool
    """
    # If we have the item at all
    if query_inventory(name = name, on_hand = on_hand):
        # If we have enough of the item
        if on_hand[name]["qty"] + qty >= 0: 
            on_hand[name]["qty"] += qty
            return True
    return False 

def adjust_price(name: str = "", price: float = 0.0, on_hand: dict = {}) -> None:
    """
    Adjust item price for an item in on_hand

    :param name: Description
    :type name: str
    :param price: Description
    :type price: int
    :param inventory: Description
    :type inventory: dict
    """
    if query_inventory(name = name, on_hand = on_hand):
        on_hand[name]["price"] = price

def calculate_sale(name: str = "", qty: int = 0, stock: dict = {}) -> None:
    """
    Docstring for calculate_sale

    :param name: Description
    :type name: str
    :param qty: Description
    :type qty: int
    :param inventory: Description
    :type inventory: dict
    """
    if adjust_qty(name = name, qty = -qty, on_hand = stock):
        income = round(stock[name]["price"] * qty , 2)
        print(f"SALE: {qty} {name} ${income}")
    else:
        print("We can't sell that many!")

def show_all(stock: dict = {}) -> None:
    """
    Docstring for show_all

    :param inventory: Description
    :type inventory: dict
    """
    print("Name\tPrice\tQuantity")
    # For each fruit in the dictionary
    for fruit in stock:
        print(f"{fruit}\t{stock[fruit]["price"]}\t{stock[fruit]["qty"]}")


def main():
    storage = {}
    while True:
        Inventory.menu()
        choice = input("Select from menu ('e' to exit): ").lower()
        if choice != "5" and choice != "e":
            item = input("Enter item name: ")
        match choice:
            case '1':
                check_item(name = item, on_hand = storage)
            case '2':
                price = float(input(f"Enter price for {item}: "))
                adjust_price(name = item, price = price, on_hand = storage)
            case '3':
                qty = int(input(f"Adjust {item} qty by: "))
                adjust_qty(name = item, qty = qty, on_hand = storage) 
            case '4':
                single_item = {item: storage[item]}
                show_all(stock = single_item)
                input("Press any key to continue...")
            case '5':
                show_all(stock = storage)
                input("Press any key to continue...")
            case '6':
                qty = int(input(f"Sell how many {item}: "))
                calculate_sale(name = item, qty = qty, stock = storage)
            case 'e':
                break
        sleep(2)


if __name__ == "__main__":
    main()
