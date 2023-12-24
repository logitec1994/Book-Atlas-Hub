from flask import Blueprint, render_template, request
import requests

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def main():
    # base_url = request.url_root
    # prefix = "/api/authorized"
    # params = {'param1': 'value1', 'param2': 'value2'}

    # req = requests.get(base_url+prefix,
    #                    params=params)
    # print(req.text)

    is_authorized = request.cookies.get("")
    if is_authorized:
        return render_template("authorized/main.tt")
    else:
        return render_template("unauthorized/main.tt")
