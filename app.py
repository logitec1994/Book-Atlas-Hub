from flask import Flask
from api.routes import api_bp
from api.routes import db, bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some_perfect_secret_key'

app.register_blueprint(api_bp)

db.init_app(app)
bcrypt.init_app(app)


if __name__ == "__main__":
    app.run(debug=True)
