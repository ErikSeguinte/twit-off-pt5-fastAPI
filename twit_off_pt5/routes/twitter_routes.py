from flask import Blueprint, render_template, jsonify
from twit_off_pt5.models import db, User, Tweet, parse_records
from twit_off_pt5.services.twitter_service import api as twitter
from twit_off_pt5.services.basilica_service import connection as basilica

twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    user = twitter.get_user(screen_name)
    statuses = twitter.user_timeline(
        screen_name,
        tweet_mode="extended",
        count=150,
        exclude_replies=True,
        exclude_retweets=True,
    )
    # return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)
    db.session.commit()
    return "OK"
