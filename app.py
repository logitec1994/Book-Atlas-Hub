from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/auth/register")
def registration():
    return "Hello registration"


if __name__ == "__main__":
    app.run(debug=True)
