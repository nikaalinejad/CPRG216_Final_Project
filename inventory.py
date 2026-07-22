#last edit: 12/13/2025

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


