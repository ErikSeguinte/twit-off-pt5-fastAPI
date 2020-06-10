from flask import Blueprint, request, jsonify, render_template

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from twit_off_pt5.core.models import User, Tweet
from twit_off_pt5.services.basilica_service import connection as basilica

stats_routes = Blueprint("stats_routes", __name__)


@stats_routes.route("/predict", methods=["post"])
def predict():
    # TODO
    data = request.form
    print(data)
    user_1 = _get_user(data["user_1"])
    user_1_embeddings = [tweet.embedding for tweet in user_1.tweets]
    user_2 = _get_user(data["user_2"])
    user_2_embeddings = [tweet.embedding for tweet in user_2.tweets]

    embeddings = []
    labels = []

    for embedding in user_1_embeddings:
        labels.append(user_1.screen_name)
        embeddings.append(embedding)

    for embedding in user_2_embeddings:
        labels.append(user_2.screen_name)
        embeddings.append(embedding)
    classifier = make_pipeline(StandardScaler(), LogisticRegression())
    classifier.fit(embeddings, labels)

    new_embedding = basilica.embed_sentence(data["text"], model="twitter")
    result = classifier.predict([new_embedding])

    return render_template(
        "results.html",
        screen_name_a=user_1.screen_name,
        screen_name_b=user_2.screen_name,
        tweet_text=data["text"],
        screen_name_most_likely=result[0],
    )


@stats_routes.route("/predict_form")
def get_usernames():
    return render_template("predict_form.html")


def _get_user(username):
    user = User.query.filter(User.screen_name == username).one()
    print(user)
    return user
