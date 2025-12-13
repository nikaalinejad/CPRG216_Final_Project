#Comments at top
#Name: Nika
#Date: 12/13/2025
'''
Program Description: This file defines the Inventory class, which manages a collection of Product objects within the mini inventory system. 
Inputs include product data loaded from a file or entered by the user, such as product ID, name, quantity, and price which become useful in part 3 when inputs are collected from the user. 
The class processes these inputs by storing products in a list and providing methods to add new products, find existing ones, sell items, and restock quantities. 
It also handles saving updated inventory data back to a file, ensuring persistence between program runs. 
Outputs are generated through method results (e.g., True/False for restock or sale success, None if product not found and printed product listings that display the current state of the inventory in a clear format.
'''

#Part 2 - Inventory Class (inventory.py)

from product import Product 

class Inventory: 
    def __init__(self):
        self.products = [] #creates an empty products list 

    def load_from_file(self, filename):
        #read file lines (formatted as: ID, Name, Quantity, Price.)
        #creates Product objects and append
        with open(filename, 'r') as file:
            for line in file: 
                parts = line.strip().split(',')
                if len(parts) == 4: #line split into exactly 4 parts
                    #assigns each part to a variable
                    product_id = parts[0]
                    name = parts[1]
                    quantity = int(parts[2])
                    price = float(parts[3])
                    product = Product(product_id, name, quantity, price) #creation of a new Product object using the values
                    self.products.append(product) #adds the Product object to the list self.products
    
    def save_to_file(self, filename):
        #save all products back to file in the same CSV format
        with open(filename, 'w') as file:
            for product in self.products:
                line = f"{product.product_id},{product.name},{product.quantity},{product.price:.2f}\n"
                file.write(line)

    def add_product(self, product):
        #append the given Product to products list
        self.products.append(product)

    def find_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product

    def sell_product(self, product_id, amount):
        product = self.find_product(product_id)
        if product is None:
            return None
        return product.sell(amount)

    def restock_product(self, product_id, amount):
        product = self.find_product(product_id)
        if product is None: 
            return False
        product.restock(amount)
        return True

    def print_all_products(self):
        #prints each product using its ___str__() output
        print("\n--- Inventory List ---")
        for product in self.products:
            print(product)
        print()


