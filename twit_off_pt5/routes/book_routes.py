from flask import Blueprint, jsonify, request, render_template
from twit_off_pt5.models import db, Book, parse_records

book_routes = Blueprint("book_routes", __name__)

@book_routes.route("/books.json")
def list_books():
    records = Book.query.all()
    books = parse_records(records)
    return jsonify(books)

@book_routes.route("/books")
def list_books_for_humans():
    records = Book.query.all()
    books = parse_records(records)
    return render_template("books.html", message="Here's some books", books=books)

@book_routes.route("/books/new")
def new_book():
    return render_template("new_book.html")

@book_routes.route("/books/create", methods=["POST"])
def create_book():
    print("FORM DATA:", dict(request.form))

    data = request.form
    breakpoint()
    
    new_book = Book(title=data["title"], author_id=data["author_id"])

    db.session.add(new_book)
    db.session.commit()


    return jsonify({
        "message": "BOOK CREATED OK (TODO)",
        "book": dict(request.form)})