#Part 2 - Inventory Class (inventory.py)

from product import Product 

#inventory class manages multiple product objects 
class Inventory: 
    def __init(self):
        #no parameters 
        #returns none
        #creates an empty products list 
        pass

    def load_from_file(self,filename):
        #parameters is a sring
        #returns none 
        #Read file lines formatted as: ID,Name,Quantity,Price. Create Product objects and append.
        pass
    
    def save_to_file(self, filename):
        #accepts string
        #returns none 
        #Save all products back to file in the same CSV format.
        pass

    def add_product(self, product):
        #parameter is product 
        #returns none 
        #appends the give product to products list.
        pass

    def find_product(self, product_id):
        #parameter is string 
        #returns product or none 
        #Return the product with matching ID or None if not found.
        pass

    def sell_product(self, product_id, amount):
        #parameter is str, int
        #returns true/false/none
        #return None if product not found; else return Product.sell(amount).
        pass

    def restock_product(self, product_id, amount):
        #parameter is str, int
        #returns true/false
        #Restock if found and return True; otherwise return False.
        pass

    def print_all_products(self):
        #no parameters 
        #return none
        #Print each product using its __str__() output.
        pass