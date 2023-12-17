from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from flask_bcrypt import Bcrypt

api_bp = Blueprint("api", __name__, url_prefix="/api")
db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           validators.InputRequired(), validators.Length(min=4, max=50)])
    password = PasswordField('Password', validators=[
                             validators.InputRequired(), validators.Length(min=6, max=100)])
    email = StringField('Email', validators=[
                        validators.InputRequired(), validators.Email()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           validators.InputRequired(), validators.Length(min=4, max=50)])
    password = PasswordField('Password', validators=[
                             validators.InputRequired(), validators.Length(min=6, max=100)])


@api_bp.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    data_from_form = request.get_json()
    data_from_form['csrf_token'] = form.csrf_token.current_token

    if not data_from_form:
        return jsonify({"error": "Empty data"}), 400

    form = RegistrationForm(data=data_from_form)

    if not form.validate():
        return jsonify({"error": form.errors}), 400

    hashed_password = bcrypt.generate_password_hash(
        form.password.data).decode('utf-8')

    new_user = User(
        username=form.username.data,
        password=hashed_password,
        email=form.email.data
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User added successfully"}), 201


@api_bp.route("/login", methods=["POST"])
def signin():
    form = LoginForm()
    data_from_form = request.get_json()
    data_from_form['csrf_token'] = form.csrf_token.current_token

    if not data_from_form:
        return jsonify({"error": "Empty data"}), 400

    form = LoginForm(data=data_from_form)

    if not form.validate():
        return jsonify({"error": form.errors}), 400

    hashed_password = bcrypt.generate_password_hash(
        form.password.data).decode('utf-8')

    user = User.query.filter_by(username=data_from_form['username']).first()

    if not user:
        return jsonify({"error": "Invalid login or password"}), 200

    return jsonify({"message": user.username})
