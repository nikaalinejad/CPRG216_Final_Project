#last edit: 12/13/2025

#Part 1 - Product Class (product.py)

class Product:
    def __init__(self, product_id, name, quantity, price):
        #initializes the product with given values
        self.product_id = product_id 
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def sell(self, amount):
        #evaluates whether quantity should decrease or not
        if self.quantity >= amount: 
            self.quantity -= amount
            return True
        else:
            return False
            
    def restock(self, amount):
        #increases quantity by amount
        self.quantity += amount 

    def __str__(self):
        #returns formatted text 
        return f"{self.product_id} | {self.name: <10} | Qty: {self.quantity: <2} | ${self.price:.2f}"

