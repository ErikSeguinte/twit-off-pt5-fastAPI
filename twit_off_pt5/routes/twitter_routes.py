from flask import Blueprint, render_template, redirect
from twit_off_pt5.core.models import db, User, Tweet
from twit_off_pt5.services.twitter_service import api as twitter
from twit_off_pt5.services.basilica_service import connection as basilica

twitter_routes = Blueprint("twitter_routes", __name__)


@twitter_routes.route("/users")
def add_users():
    return render_template("user_form.html")

@twitter_routes.route("/user", methods = ['post'])
def redirect_user():
    username = requests.form['username']
    return redirect(f"/users/{username}")


@twitter_routes.route("/users/<screen_name>")
def get_user(screen_name=None):
    print(screen_name)
    user = twitter.get_user(screen_name)
    statuses = twitter.user_timeline(
        screen_name,
        tweet_mode="extended",
        count=150,
        exclude_replies=True,
        exclude_rts=True,
    )
    # return jsonify({"user": user._json, "tweets": [s._json for s in statuses]})

    db_user = User.query.get(user.id) or User(id=user.id)
    db_user.screen_name = user.screen_name
    db_user.name = user.name
    db_user.location = user.location
    db_user.followers_count = user.followers_count
    db.session.add(db_user)

    all_tweet_texts = [status.full_text for status in statuses]
    embeddings = list(basilica.embed_sentences(all_tweet_texts, model="twitter"))

    for status, embedding in zip(statuses, embeddings):
        if not Tweet.query.get(status.id):
            db_tweet = Tweet(id=status.id)
            db_tweet.user_id = db_user.id
            db_tweet.full_text = status.full_text
            db_tweet.embedding = embedding
            db.session.add(db_tweet)
    db.session.commit()
    return render_template(
        "user.html", user=db_user, tweets=statuses
    )  # tweets=db_tweets
