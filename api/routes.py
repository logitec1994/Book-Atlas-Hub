from flask import Blueprint, make_response

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/registration", methods=["POST"])
def registration():
    resp = make_response("Cookie set")
    resp.set_cookie("registration_cookie", "Alex")
    return resp


@api_bp.route("/login", methods=["POST"])
def signin():
    return "Hello signin"
