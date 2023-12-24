from flask import Blueprint, render_template, request, redirect
import requests

user_bp = Blueprint("user", __name__)


@user_bp.route("/profile")
def profile_page():
    is_authorized = request.cookies.get("user")
    if is_authorized:
        return redirect("/")
    else:
        return render_template("unauthorized/profile.tt")


@user_bp.route("/auth")
def auth_page():
    is_authorized = request.cookies.get("user")
    if is_authorized:
        return redirect("/")
    else:
        return render_template("unauthorized/auth.tt")


@user_bp.route("/auth", methods=["POST"])
def user_data_handler():
    user_data = request.get_json()
    base_url = request.url_root
    prefix = "/api/users/"
    req = requests.get(base_url+prefix+user_data['login'])
    print(req)
    if req.status_code == 404:
        return req.json()['message']
    # print(f"This is {req.json()['user_id']}")
    if req:
        resp = redirect("/")
        resp.headers['HX-Redirect'] = '/'
        resp.set_cookie("user", str(req.json()['user_id']), max_age=600)
        return resp
    return "Default answer"
