#Comments at top 
#Name: Nika
#Date: 12/13/2025
'''
Program Description: This file defines the Product class, which represents individual items in the inventory system. 
Inputs to the class include product details such as ID, name, quantity, and price, and are collected later in the program in a seperate document (part 3) provided when creating a new Product object. 
The class processes these inputs by storing them as attributes and offering methods to update the product’s state, such as selling items (which decreases quantity if enough stock exists) or restocking items (which increases quantity). 
Outputs are returned through method results (e.g., True/False for successful sales) and a formatted string representation of the product, which displays its ID, name, quantity, and price in a clear, readable format.
'''

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
        return f"{self.product_id} | {self.name: <10} | Qty: {self.quantity: <2} | ${self.price:.2f}"
