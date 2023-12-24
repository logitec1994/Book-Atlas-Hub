from flask import Blueprint, request, jsonify
from .database.db_handler import create_user, get_user_by_username


api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/users")
def get_users():
    return "List of all users"


@api_bp.route("/users/<username>")
def get_user(username):
    user = get_user_by_username(username)
    if user:
        return jsonify({"user_id": user[0]})
    return jsonify({"message": "user not found"}), 404


@api_bp.route("/users", methods=["POST"])
def add_user():
    user_data = request.get_json()
    create_user(user_data.get("login"), user_data.get(
        "password"), user_data.get("email"))
    return "User successfully added"


@api_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return f"User {user_id} were successfully updated"


@api_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return f"User {user_id} were successfully deleted"
