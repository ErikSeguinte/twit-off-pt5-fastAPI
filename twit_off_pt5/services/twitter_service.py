import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("twitter_api")
api_secret = os.getenv('twitter_secret')
access = os.getenv('twitter_access')
access_secret = os.getenv('twitter_access_secret')

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access, access_secret)

api = tweepy.API(auth)

user = api.get_user('primefactorx01')
print(type(user))
breakpoint()
