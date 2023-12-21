from flask import Flask
from api.routes import api_bp
from server.routes import server_bp

app = Flask(__name__, template_folder="server/templates",
            static_folder="server/static")

app.register_blueprint(api_bp)
app.register_blueprint(server_bp)


if __name__ == "__main__":
    app.run(debug=True)
