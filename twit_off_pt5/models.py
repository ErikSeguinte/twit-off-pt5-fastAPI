from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from pathlib import Path

db = SQLAlchemy()
migrate = Migrate()




class Book(db.Model):
    Column = db.Column
    Integer = db.Integer
    String = db.String
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    author_id = Column(String(128))

    def __repr__(self):
        return f"<Book {self.id} {self.title}>"

def parse_records(dabatabase_records):
    pass
