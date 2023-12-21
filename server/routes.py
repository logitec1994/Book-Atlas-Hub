from flask import Blueprint, render_template, request, redirect

server_bp = Blueprint("server", __name__)


@server_bp.route("/")
def main_page():
    return render_template("main.html", title="Main page")


@server_bp.route("/registration")
def registration_page():
    is_auth = request.cookies.get("sing")
    if is_auth:
        redirect("/")
    return render_template("registration.html", title="Registration page")
