#Part 3 - Main Program (main.py)
#driver of the entire program 
''' it will 1. Create an Inventory object
2. Load products from inventory.csv
3. Show a menu
4. Call the correct Inventory methods depending on the menu option
5. Save the updated inventory before exiting
The program stays running until the user chooses option 5. '''

#required menu
'''
Your menu must look like this:
--- Mini Inventory System ---
1. Add Product
2. Sell Product
3. Restock Product
4. Show All Products
5. Exit and Save
You must use input() to read the option.

What Each Menu Option Should Do
1. Add Product
 Ask the user for product ID, name, quantity, and price
 Create a Product object
 Add it using inventory.add_product(product)
2. Sell Product
 Ask for product ID and amount
 Call inventory.sell_product(product_id, amount)
 Output message based on returned value
3. Restock Product
 Ask for product ID and amount
 Call inventory.restock_product(product_id, amount)
4. Show All Products
 Call inventory.print_all_products()
5. Exit and Save
 Call inventory.save_to_file("inventory.csv")
 End the program
'''

#minimal template skeleton of main program

from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()
    filename = "inventory.csv"
     # Load existing data
    inventory.load_from_file(filename)
    while True:
        print("\n--- Mini Inventory System ---")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. Restock Product")
        print("4. Show All Products")
        print("5. Exit and Save")
        
        choice = input("Choose an option: ")
        if choice == "1":
            # Add product
            pass
        elif choice == "2":
            # Sell product
            pass
        elif choice == "3":
            # Restock product
            pass
        elif choice == "4":
            # Show products
            pass
        elif choice == "5":
            # Save and exit
            pass
        else:
            print("Invalid choice. Try again.")

#Students must fill each pass section correctly, using the Inventory class methods.