#Part 3 - Main Program (main.py)
#driver of the entire program 

from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()
    filename = "inventory.csv"
     # Load existing data
    inventory.load_from_file(filename)

    #I'm swtiching the skeleton template which includes while true, to a different control/loop/whatever since the assignment prefers not to use while True or while flag particularly if there is a clear loop condition(s)
    choice = "" #constant/initial val
        print("\n--- Mini Inventory System ---")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. Show All Products")
        print("5. Exit and Save")

    while choice != "5":
        choice = input("Choose an option: ")

        match choice: 
            case "1":
            # Add product
            pass
         case "2":
            # Sell product
            pass
        case "3":
            # Restock product
            pass
        case "4":
            # Show products
            pass
        case "5":
            # Save and exit
            pass
        case _:
            print("Invalid choice. Try again.")


#Students must fill each pass section correctly, using the Inventory class methods.
