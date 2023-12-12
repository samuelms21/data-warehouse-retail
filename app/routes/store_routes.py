from flask import Blueprint, request, jsonify
from app.models.store_model import Store

store_bp = Blueprint('store_bp', __name__)

@store_bp.route('/stores', methods=['GET'])
def get_stores():
    stores = Store.query.all()
    return jsonify(stores), 200
