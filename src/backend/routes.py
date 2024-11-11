from flask import Blueprint, request, jsonify, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from database import get_clickhouse_client
from utils import hash_password, check_password
from models import User

client = get_clickhouse_client()

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    is_seller = data.get('is_seller')
    id_employee = data.get('id_employee')

    if User.get_user_by_email(email):
        return jsonify({'message': 'Usuário já existe'}), 409

    hashed_password = hash_password(password)
    
    User.insert_user(email, username, hashed_password, is_seller, id_employee)

    return jsonify({'message': 'Usuário registrado com sucesso'}), 201

@auth.route('/login', methods=['POST'])
def login() -> dict:
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.get_user_by_email(email)

    if not user or not check_password(password, user[0][2]):  # user[0][1] é o password_hash
        return jsonify({'message': 'Nome de usuário ou senha incorretos'}), 401

    access_token = create_access_token(identity=email)
    # return jsonify(access_token=access_token), 200

    return jsonify(
        email=user[0][0],  # Email
        username=user[0][1],  # Username
        is_seller=user[0][3],  # Seller
        id_employee = user[0][4],  # Employee ID
        access_token = access_token  # JWT
    )

@auth.route("/who_am_i", methods=["GET"])
@jwt_required()
def protected():
    current_user_email = get_jwt_identity()
    user = User.get_user_by_email(current_user_email)
    if user:
        return jsonify(
            email=user[0][0],  # Email
            username=user[0][1],  # Username
            is_seller=user[0][3],  # Seller
            id_employee = user[0][4]  # Employee ID
        )
    return jsonify({"msg": "Usuário não encontrado"}), 404

view = Blueprint('view', __name__)
    
@view.route('/inventory', methods=['GET'])
@jwt_required()
def get_inventory_view() -> dict:
    try:
        query = f"SELECT * FROM vw_inventory"
        result = client.query(query)
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@view.route('/seller_progress/<id_seller>', methods=['GET'])
@jwt_required()
def get_seller_progress_view(id_seller: int) -> dict:
    try:
        query = f"SELECT tb_employee.id, tb_transactions.date, total_sales, tb_target_salesperson.target FROM vw_seller_progress WHERE tb_employee.id = {id_seller}"
        result = client.query(query)
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@view.route('/seller_ranking', methods=['GET'])
@jwt_required()
def get_sellers_ranking_view() -> dict:
    try:
        query = f"SELECT * FROM vw_sellers_ranking"
        result = client.query(query)
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@view.route('/store_progress/<id_store>', methods=['GET'])
@jwt_required()
def get_store_progress_view(id_store: int) -> dict:
    try:
        query = f"SELECT tb_store.id, tb_transactions.date, total_sales, tb_target_store.target FROM vw_store_progress WHERE tb_store.id = {id_store}"
        result = client.query(query)
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@view.route('/store_ranking', methods=['GET'])
@jwt_required()
def get_store_ranking_view() -> dict:
    try:
        query = f"SELECT * FROM vw_stores_ranking"
        result = client.query(query)
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@view.route('/top_products', methods=['GET'])
@jwt_required()
def get_top_products_view() -> dict:
    try:
        query = f"SELECT * FROM vw_top_products"
        result = client.query(query)
        return jsonify(result.result_rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500