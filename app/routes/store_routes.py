from flask import Blueprint, request, jsonify
from app.models.store_model import Store
from app.services.store_service import StoreService

store_bp = Blueprint('store_bp', __name__)

@store_bp.route('/stores', methods=['GET'])
def get_stores():
    stores = StoreService.get_all_stores()
    return jsonify(stores), 200
