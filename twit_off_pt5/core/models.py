from sqlalchemy import create_engine, Boolean, Column, BigInteger, Integer, ForeignKey, String, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DB_URI = "postgres://wbakakfzhirkzk:85e2c6305a72c6aef469b01910aae3b04188511880434c08f5fd163ca81c41ea@ec2-35-169-254-43.compute-1.amazonaws.com:5432/df5orp7bpp1h3n"

engine = create_engine(DB_URI)

SessionLocal=sessionmaker(autocommit=False, autoflash=False, bind=engine)

Model = declarative_base()


class User(Model):
    __tablename__="user"
    id = Column(BigInteger, primary_key=True)
    screen_name = Column(String(128), nullable=False)
    location = Column(String(128))
    followers_count = Column(Integer)


class Tweet(Model):
    __tablename__="tweet"
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("user.id"))
    full_text = Column(String(500))
    embedding = Column(PickleType)

    user = relationship("User", backref=backref("tweets", lazy=True), cascade = "all, delete-orphan", single_parent=True)


class Admin(Model):
    __tablename__="admin"
    username = Column(String, primary_key=True)
    api_key = Column(String, nullable=False)


# def parse_records(database_records):
#     """
#     A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

#     Param: database_records (a list of db.Model instances)

#     Example: parse_records(User.query.all())

#     Returns: a list of dictionaries, each corresponding to a record, like...
#         [
#             {"id": 1, "title": "Book 1"},
#             {"id": 2, "title": "Book 2"},
#             {"id": 3, "title": "Book 3"},
#         ]
#     """
#     parsed_records = []
#     for record in database_records:
#         print(record)
#         parsed_record = record.__dict__
#         del parsed_record["_sa_instance_state"]
#         parsed_records.append(parsed_record)
#     return parsed_records
