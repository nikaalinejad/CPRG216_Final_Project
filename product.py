#Part 1 - Product Class (product.py)

class Product:
    #requjired methods 
    #__init__
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id #should be entered as a string later
        self.name = name #should be entered as a string later
        self.quantity = quantity #should be entered as a integer later
        self.price = price #should be entered as a float later
        #returns none 
        #initializes the product with given values
        pass

    #sell
    def sell(self, amount):
        #returns true/false 
        #accepts integer parameter 
        #if quanitity >= amount, decrease quantity and return True; otherwise return False.
        #use if/else statement for this
        pass
    
    #restock 
    def restock(self, amount):
        #returns none 
        #accepts integer parameter 
        #Increases quantity by amount 
        pass

    #__str))
    def __str__(self):
        #no parameters
        #returns string 
        #Return formatted text: 'P001 | Laptop | Qty: 10 $999.99'
        pass
    