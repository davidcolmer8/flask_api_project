from flask import Flask
from bookStore/books/book.py
def create_app():
    app = Flask('bookStore', static_folder=None)
    return app



