from flask import Blueprint, render_template, jsonify
from twit_off_pt5.services.twitter_service import api

twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    user = api.get_user(screen_name)
    statuses = api.user_timeline(
        screen_name,
        tweet_mode="extended",
        count=150,
        exclude_replies=True,
        exclude_retweets=True,
    )
    return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})
