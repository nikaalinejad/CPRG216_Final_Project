#Part 2 - Inventory Class (inventory.py)

from product import Product 

class Inventory: 
    def __init__(self):
        self.products = [] #creates an empty products list 

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file: 
                parts = line.strip().split(',')
                if len(parts) == 4:
                    product_id = parts[0]
                    name = parts[1]
                    quantity = int(parts[2])
                    price = float(parts[3])
                    product = Product(product_id, name, quantity, price)
                    self.products.append(product)
    
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for product in self.products:
                line = f"{product.product_id},{product.name},{product.quantity},{product.price:.2f}\n"
                file.write(line)

    def add_product(self, product):
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
        for product in self.products:
            print(product)


