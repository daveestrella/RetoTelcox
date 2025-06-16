from flask import Blueprint, jsonify
import random

consumo_bp = Blueprint('consumo', __name__, url_prefix='/api/consumo')

@consumo_bp.route('/<cliente_id>', methods=['GET'])
def get_consumo(cliente_id):
    data = {
        "cliente_id": cliente_id,
        "nombre": f"Cliente {cliente_id}",
        "datos_consumidos_gb": round(random.uniform(0, 10), 2),
        "minutos_consumidos": random.randint(0, 500),
        "saldo_actual": round(random.uniform(0, 30), 2)
    }
    return jsonify(data)
