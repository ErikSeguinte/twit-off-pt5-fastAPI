__version__ = "0.1.0"

from flask import Flask
from pathlib import Path

from twit_off_pt5.routes.home_routes import home_routes
from twit_off_pt5.routes.book_routes import book_routes
from twit_off_pt5.routes.twitter_routes import twitter_routes
from twit_off_pt5.routes.admin_routes import admin_routes
from twit_off_pt5.routes.stats_routes import stats_routes
from twit_off_pt5.core.models import db, migrate

# db_path = Path("web_app.db")
# db_uri = "sqlite:/" + db_path.resolve().as_uri()[5:]
db_uri = "postgres://wbakakfzhirkzk:85e2c6305a72c6aef469b01910aae3b04188511880434c08f5fd163ca81c41ea@ec2-35-169-254-43.compute-1.amazonaws.com:5432/df5orp7bpp1h3n"


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
    breakpoint()
