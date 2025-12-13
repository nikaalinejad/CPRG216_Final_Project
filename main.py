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
            product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                quantity = int(input("Enter quanitity: "))
                price = float(input("Enter price: "))
                product = Product(product_id, name, quantity, price)
                inventory.add_product(product)
                print("Product added!")

         case "2":
            # Sell product
            product_id = input("Enter product ID to sell: ")
                amount = int(input("Enter amount to sell: "))
                result = inventory.sell_product(product_id, amount)
                if result is None: 
                    print("Product not found.")
                elif result: 
                    print("Sale successful!")
                else: print("Not enough stock!")
                    
        case "3":
            # Restock product
            product_id = input("Enter product ID to restock: ")
                amount = int(input("Enter amount to add: "))
                success = inventory.restock_product(product_id, amount)
                if success: 
                    print("Restocked!")
                else: 
                    print("Product not found.")
                    
        case "4":
            # Show products
            inventory.print_all_products()

        case "5":
            # Save and exit
            inventory.save_to_file(filename)
                print("Inventory saved. Goodbye!")

        case _:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main() #runs the program
