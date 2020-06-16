from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    screen_name: str
    location: str
    followers_count: int

class UserCreate(UserBase):
    pass


class TweetBase(BaseModel):
    full_text: str

class TweetCreate(TweetBase):
    pass

class Tweet(TweetBase):
    id: int
    user_id:int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    tweets: List[Tweet] = []

    class Config:
        orm_mode = True