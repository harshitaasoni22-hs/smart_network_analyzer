from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
import hashlib

auth_bp = Blueprint("auth", __name__)

USERS = {"admin": hashlib.sha256(b"admin123").hexdigest()}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    hashed = hashlib.sha256(data.get("password","").encode()).hexdigest()
    if USERS.get(data.get("username","")) == hashed:
        return jsonify(access_token=create_access_token(identity=data["username"]))
    return jsonify({"error": "Invalid credentials"}), 401