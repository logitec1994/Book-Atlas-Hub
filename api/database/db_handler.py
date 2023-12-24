import sqlite3

DB_FILE = "book_hub.db"


def create_users_table() -> None:
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


def create_user(login, password, email) -> None:
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
INSERT INTO users (username, password, email) VALUES (?, ?, ?)
""", (login, password, email)
    )
    conn.commit()
    conn.close()


def get_user_by_username(username):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.execute("""
SELECT id FROM users WHERE username = ?
""", (username,))
    return cur.fetchone()
