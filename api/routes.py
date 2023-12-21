from flask import Blueprint, jsonify, request
import sqlite3

DB_FILE = "book_hub.db"

api_bp = Blueprint("api", __name__, url_prefix="/api")


def create_table():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    email TEXT
)
""")

    conn.commit()
    conn.close()


def create_user(login, password, email):
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
INSERT INTO users (username, password, email) VALUES (?, ?, ?)
""", (login, password, email)
    )
    conn.commit()
    conn.close()


@api_bp.route("/registration", methods=["POST"])
def registration():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Empty data"}), 400

    create_user(data["login"], data["password"], data["email"])

    return jsonify({"message": "Registration successful!"}), 201
