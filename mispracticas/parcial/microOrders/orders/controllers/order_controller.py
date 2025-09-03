from flask import Blueprint, request, jsonify, session
from orders.models.order_model import Order
from db.db import db
import requests
from decimal import Decimal, ROUND_HALF_UP

order_controller = Blueprint('order_controller', __name__)

@order_controller.route('/api/orders/<int:order_id>', methods=['DELETE', 'OPTIONS'])
def delete_order(order_id):
    if request.method == 'OPTIONS':
        # Responder al preflight CORS
        return '', 204

    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

@order_controller.route('/api/orders', methods=['GET', 'POST', 'OPTIONS'])
def orders_collection():
    if request.method == 'GET':
        # Listar órdenes
        orders = Order.query.all()
        return jsonify([o.to_dict() for o in orders]), 200

    if request.method == 'POST':
        # === tu lógica actual de creación (resumen robusto) ===
        data = request.get_json(silent=True) or {}
        if 'username' not in session:
            return jsonify({'message': 'Sesión no iniciada'}), 401

        user_name = session['username']
        user_email = session.get('email', '')

        def _get_int(d, *keys):
            for k in keys:
                v = d.get(k)
                if v is None:
                    continue
                try:
                    return int(v)
                except (ValueError, TypeError):
                    pass
            return None

        items = data.get('products') or data.get('items') or []
        if not isinstance(items, list) or not items:
            return jsonify({'message': 'Falta o es inválida la información de los productos'}), 400

        total = Decimal('0.00')
        updates = []

        for it in items:
            pid = _get_int(it, 'product_id', 'id', 'productId')
            qty = _get_int(it, 'quantity', 'qty', 'cantidad', 'count')
            if not pid or not qty or qty <= 0:
                continue

            r = requests.get(f'http://microProducts:5003/api/products/{pid}', timeout=5)
            if r.status_code != 200:
                return jsonify({'message': f'Producto no encontrado: {pid}'}), 404
            p = r.json()
            available = _get_int(p, 'quantity')
            price = Decimal(str(p.get('price', 0)))
            if available is None or available < qty:
                return jsonify({'message': f'Sin stock de {pid}. Disponible {available}, solicitado {qty}'}), 400

            total += (price * qty)
            updates.append({'product_id': pid, 'new_quantity': available - qty})

        if not updates:
            return jsonify({'message': 'La orden no contiene productos válidos'}), 400

        for u in updates:
            r = requests.put(
                f'http://microProducts:5003/api/products/{u["product_id"]}',
                json={'quantity': u['new_quantity']},
                timeout=5
            )
            if r.status_code != 200:
                return jsonify({'message': f'Error al actualizar inventario del producto {u["product_id"]}'}), 500

        total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        new_order = Order(userName=user_name, userEmail=user_email, saleTotal=total)
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Orden creada exitosamente', 'order_id': new_order.id, 'saleTotal': str(total)}), 201

    # OPTIONS
    return '', 204

