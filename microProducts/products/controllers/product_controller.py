# products/controllers/product_controller.py
from flask import Blueprint, request, jsonify
from products.models.product_model import Product
from db.db import db

product_controller = Blueprint('product_controller', __name__)

@product_controller.route('/api/products', methods=['GET'])
def get_products():
    """Obtener todos los productos"""
    products = Product.query.all()
    return jsonify([product.to_frontend_dict() for product in products])

@product_controller.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Obtener un producto por ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_frontend_dict())

@product_controller.route('/api/products', methods=['POST'])
def create_product():
    """Crear un nuevo producto"""
    data = request.json
    
    # Validación básica
    if not data.get('name') or not data.get('price'):
        return jsonify({'error': 'Nombre y precio son requeridos'}), 400
    
    # Crear nuevo producto
    new_product = Product(
        name=data['name'],
        price=int(data['price']),
        quantity=int(data.get('quantity', 0))
    )
    
    db.session.add(new_product)
    db.session.commit()
    
    return jsonify({'message': 'Producto creado exitosamente', 'product': new_product.to_frontend_dict()}), 201

@product_controller.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Actualizar un producto existente"""
    product = Product.query.get_or_404(product_id)
    data = request.json
    
    # Actualizar campos
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = int(data['price'])
    if 'quantity' in data:
        product.quantity = int(data['quantity'])
    
    db.session.commit()
    
    return jsonify({'message': 'Producto actualizado exitosamente', 'product': product.to_frontend_dict()})

@product_controller.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Eliminar un producto"""
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    
    return jsonify({'message': 'Producto eliminado exitosamente'})
