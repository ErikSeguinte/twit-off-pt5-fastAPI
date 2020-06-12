from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pathlib import Path

db = SQLAlchemy()
migrate = Migrate()
Model = db.Model
Column = db.Column
Integer = db.Integer
String = db.String
BigInteger = db.BigInteger


class User(Model):
    id = Column(BigInteger, primary_key=True)
    screen_name = Column(String(128), nullable=False)
    location = Column(String(128))
    followers_count = Column(Integer)


class Tweet(Model):
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, db.ForeignKey("user.id"))
    full_text = Column(String(500))
    embedding = Column(db.PickleType)

    user = db.relationship("User", backref=db.backref("tweets", lazy=True), cascade = "all, delete-orphan", single_parent=True)


class Admin(Model):
    username = Column(String, primary_key=True)
    api_key = Column(String, nullable=False)


def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
