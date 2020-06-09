from twit_off_pt5.core.security import pwd_context, create_api_key
from twit_off_pt5.core.models import Admin, db
from flask import Blueprint, jsonify, request, render_template, flash, redirect

admin_routes = Blueprint("admit_routes", __name__)

@admin_routes.route("/admin/db/reset")
def reset_page():
    password = "Correct Horse Battery Staple"
    username = "ADMIN"
    db_user = Admin.query.get(username.lower())
    return jsonify({
        "username": username.lower(),
        "password": password,
        "access granted": pwd_context.verify(password, db_user.api_key)})