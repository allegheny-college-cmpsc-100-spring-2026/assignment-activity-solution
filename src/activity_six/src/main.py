from time import sleep
from Shop import Inventory

def query_inventory(name: str = "", inventory: dict = {}) -> bool:
    if name in inventory:
        return True
    return False

def add_item(name: str = "", inventory: dict = {}) -> bool:
    if not query_inventory(name, inventory):
        inventory[name] = {"price": 0, "qty": 0}
        return True
    return False

def check_item(name: str = "", inventory: dict = {}) -> dict:
    if not query_inventory(name, inventory):
        response = input(f"Add {name} to inventory? ").lower()
        if response == "y":
            add_item(name, inventory)

def adjust_qty(name: str = "", qty: int = 0, inventory: dict = {}):
    if inventory[name]["qty"] > 0:
        inventory[name]["qty"] -= qty

def show_all(inventory: dict = {}) -> None:
    print("Name\tPrice\tQuantity")
    for item in inventory:
        print(f"{item}\t{inventory[item]["price"]}\t{inventory[item]["qty"]}")

def main():
    inventory = {}
    choice = str()
    delay = 1
    while True:
        Inventory.menu()
        choice = input("Select from menu ('e' to exit): ").lower()
        if choice == "e":
            break
        if choice != "5":
            item = input("Enter name of item: ").lower()
        match choice:
            case "1":
                check_item(name = item, inventory = inventory)
            case "2":
                check_item(name = item, inventory = inventory)
                price = float(input("Enter price: $"))
                inventory[item]["price"] = price
            case "3":
                check_item(name = item, inventory = inventory)
                qty = int(input("Enter qty: "))
                adjust_qty(name = item, qty = qty, inventory = inventory)
            case "4":
                check_item(name = item, inventory = inventory)
                show_all({item: inventory[item]})
            case "5":
                show_all(inventory)
            case "6":
                check_item(name = item, inventory = inventory)
                qty = int(input("Enter quantity to sell: "))
                adjust_qty(name = item, qty = qty, inventory = inventory)
                print(f"SALE: {qty} {item}: {inventory[item]["qty"] * qty}")
            case _:
                pass
        sleep(delay)


if __name__ == "__main__":
    main()