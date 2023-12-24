from flask import render_template


def not_found_page(error):
    return render_template("not_found.tt", error=error), 404
