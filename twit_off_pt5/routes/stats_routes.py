from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegressionCV

from twit_off_pt5.core.models import User, Tweet
from twit_off_pt5.services.basilica_service import connection as basilica

stats_routes= Blueprint("stats_routes", __name__)


@stats_routes.route("/predict", methods=["post"])
def predict():
    # TODO
    data = request.form
    print(data)
    return "TODO: PREDICTING"


@stats_routes.route("/predict_form")
def get_usernames():
    return render_template("predict_form.html")
