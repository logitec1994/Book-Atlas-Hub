from flask import Blueprint, render_template, request, redirect, make_response, url_for
import requests

server_bp = Blueprint("server", __name__)


@server_bp.route("/")
def main_page():
    cook = request.cookies.get("manual")
    if not cook:
        return render_template("main.tt", title="Main page")
    return render_template("main.tt", title="Main page", cookie=cook, name=cook)


@server_bp.route("/registration", methods=["GET", "POST"])
def registration_page():
    if request.method == "GET":
        if not request.cookies.get("manual"):
            return render_template("registration.tt", title="Registration page")
        return redirect("/")

    if request.method == "POST":
        user_data = request.get_json()
        base_url = request.url_root
        headers = {"Content-Type": "application/json"}
        response = requests.post(
            url=base_url+"/api/registration", headers=headers, json=user_data)

        print(response.json()['message'])

        cook = make_response(response.json()['message'])
        cook.headers['HX-Redirect'] = '/'
        cook.set_cookie(
            "manual", user_data['login'], max_age=300, samesite=None)
        return cook


@server_bp.route("/logout")
def logout():
    resp = redirect("/")
    resp.delete_cookie("manual")

    return resp
