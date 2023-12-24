from flask import Flask
from api.routes import api_bp
from server.main_page import main_bp
from server.user import user_bp
from server.errors import not_found_page

app = Flask(__name__, template_folder="server/templates",
            static_folder="server/static")

# API routes
app.register_blueprint(api_bp)

# Web routes
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)


app.errorhandler(404)(not_found_page)


if __name__ == "__main__":
    app.run(debug=True)
