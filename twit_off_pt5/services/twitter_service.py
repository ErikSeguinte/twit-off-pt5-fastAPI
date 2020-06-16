import tweepy
import os
from dotenv import load_dotenv

cursor = tweepy.Cursor

load_dotenv()

api_key = os.getenv("twitter_api")
api_secret = os.getenv("twitter_secret")
access = os.getenv("twitter_access")
access_secret = os.getenv("twitter_access_secret")

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access, access_secret)

api = tweepy.API(auth)

if __name__ == "__main__":
    user = api.get_user("primefactorx01")
    print(type(user))

    tweets = api.user_timeline(
        "primefactorx01",
        tweet_mode="extended",
        exclude_replies=True,
        exclude_retweets=True,
    )
    breakpoint()
