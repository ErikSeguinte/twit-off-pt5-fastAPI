from flask import Blueprint, redirect, url_for

home_routes = Blueprint("home_routes", __name__)


@home_routes.route("/")
def index():
    x = 2 + 2
    return redirect(url_for("stat_routes.get_usernames"))


@home_routes.route("/about")
def about():
    return "About me"
