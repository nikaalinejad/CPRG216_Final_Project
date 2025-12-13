#Part 1 - Product Class (product.py)

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id 
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def sell(self, amount):
        if self.quantity >= amount: 
            self.quantity -= amount
            return True
        else:
            return False
            
    def restock(self, amount):
        self.quantity += amount 

    def __str__(self):
        return f"{self.product_id} | {self.name: <10} | Qty: {self.quantity: <3} | ${self.price:.2f}"

