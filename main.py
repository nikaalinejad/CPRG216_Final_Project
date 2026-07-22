#last edit: 07/21/2026

#Part 3 - Main Program (main.py)
#This segment of the project serves the purpose of being the driver of the entire program 
#The classes from inventory.py and product.py are imported and used when the main() is run
#In the main function information is collected to then be able to be processed by the program all together to provide meaningful output for the user. 

from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()
    filename = "inventory.csv"
     #load existing data
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
            #add product
                product_id = input("Enter product ID: ")
                name = input("Enter product name: ")
                quantity = int(input("Enter quanitity: "))
                price = float(input("Enter price: "))
                product = Product(product_id, name, quantity, price)
                inventory.add_product(product)
                print("Product added!\n")

            case "2":
                #sell product
                    product_id = input("Enter product ID to sell: ")
                    amount = int(input("Enter amount to sell: "))
                    result = inventory.sell_product(product_id, amount)
                    if result is None: 
                        print("\nProduct not found.\n")
                    elif result: 
                        print("\nSale successful!\n")
                    else: print("\nNot enough stock!\n")
                    
            case "3":
                #restock product
                    product_id = input("Enter product ID to restock: ")
                    amount = int(input("Enter restock amount: "))
                    success = inventory.restock_product(product_id, amount)
                    if success: 
                        print("\nRestocked!\n")
                    else: 
                        print("\nProduct not found.\n")
                    
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
    main() #run

