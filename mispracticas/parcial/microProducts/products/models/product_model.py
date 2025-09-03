# products/models/product_model.py
from db.db import db

class Product(db.Model):
     __tablename__ = 'products'  # <-- Especifica explícitamente el nombre de la tabla
    
     id = db.Column(db.Integer, primary_key=True)   
     name = db.Column(db.String(255), nullable=True)  # varchar(255) en MySQL
     price = db.Column(db.Integer, nullable=True)     # int en MySQL
     quantity = db.Column(db.Integer, nullable=True)  # int en MySQL

     def __init__(self, name, price, quantity):
         self.name = name
         self.price = price
         self.quantity = quantity

     def to_dict(self):
         return {
             'id': self.id,
             'name': self.name,
             'price': self.price,
             'quantity': self.quantity
         }

     def to_frontend_dict(self):
         """Método para convertir a formato esperado por frontend"""
         return {
             'id': self.id,
             'name': self.name,
             'price': self.price,
             'quantity': self.quantity
         }
