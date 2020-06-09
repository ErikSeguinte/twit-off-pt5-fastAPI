from twit_off_pt5.core.security import pwd_context, create_api_key
from twit_off_pt5.core.models import Admin, db
from flask import Blueprint, jsonify, request, render_template, flash, redirect, abort
from os import getenv

admin_routes = Blueprint("admit_routes", __name__)

@admin_routes.route("/admin/db/reset_confirmation")
def reset_page():
    password = getenv("db_api_key")
    username = "ADMIN"
    db_user = Admin.query.get(username.lower())
    # return jsonify({
    #     "username": username.lower(),
    #     "password": password,
    #     "access granted": pwd_context.verify(password, db_user.api_key)})
    
    return render_template("reset.html")


@admin_routes.route("/admin/db/reset", methods=["post"])
def reset():
    data = request.form
    db_user = Admin.query.get(data['username'].lower())
    if db_user:
        if pwd_context.verify(data["api_key"], db_user.api_key):
            return("RESETTING DB")
    abort(403)
