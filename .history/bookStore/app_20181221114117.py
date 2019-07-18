from flask import Flask
from bookStore/booksbook import book
def create_app():
    app = Flask('bookStore', static_folder=None)
    return app



