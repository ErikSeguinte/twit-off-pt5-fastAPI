from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from twit_off_pt5.core import models, pydantic_models
from ..services.twitter_service import api as twitter
from ..services.twitter_service import cursor
from sqlalchemy.orm import Session
# from twit_off_pt5.services.basilica_service import connection as basilica

twitter_routes = APIRouter()
templates = Jinja2Templates(directory="templates")


@twitter_routes.get("/users")
def add_users(request:Request):
    return templates.TemplateResponse("user_form.html", {"request":request})


@twitter_routes.post("/user")
def redirect_user(user:str = Form("user")):
    url = f"/users/{user}"
    response = RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    return response

@twitter_routes.get("/test/user", response_model=pydantic_models.User)
def print_user(db:Session = Depends(models.get_db)):
    sn = "primefactorx01"
    db_user = get_db_user(db, sn)
    breakpoint()
    return db_user

def get_db_user(db:Session = Depends(models.get_db), screen_name:str = "primefactorx01"):
    breakpoint()
    return db.query(models.User).filter(models.User.screen_name ==screen_name).first()

@twitter_routes.get("/users/{screen_name}")
def get_user(screen_name=None, db:Session = Depends(models.get_db)):
    print(screen_name)
    user = twitter.get_user(screen_name)
    statuses = [status._json['full_text'] for status in cursor(twitter.user_timeline,
        screen_name = screen_name,
        tweet_mode="extended",
        exclude_replies=True,
        exclude_rts=True,
    ).items(50)]

    # return {'Number of Tweets':len(statuses), "user": user._json, "tweets": statuses}

    db_user = get_db_user(db, screen_name)
#     db_user.screen_name = user.screen_name
#     db_user.name = user.name
#     db_user.location = user.location
#     db_user.followers_count = user.followers_count
#     db.session.add(db_user)

#     all_tweet_texts = [status.full_text for status in statuses]
#     embeddings = list(basilica.embed_sentences(all_tweet_texts, model="twitter"))

#     for status, embedding in zip(statuses, embeddings):
#         if not Tweet.query.get(status.id):
#             db_tweet = Tweet(id=status.id)
#             db_tweet.user_id = db_user.id
#             db_tweet.full_text = status.full_text
#             db_tweet.embedding = embedding
#             db.session.add(db_tweet)
#     db.session.commit()
#     return render_template(
#         "user.html", user=db_user, tweets=statuses
#     )  # tweets=db_tweets
