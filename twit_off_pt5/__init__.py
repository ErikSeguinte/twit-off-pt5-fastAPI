__version__ = '0.1.0'
import jinja2
from flask import Flask

from twit_off_pt5.routes.home_routes import home_routes
from twit_off_pt5.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)