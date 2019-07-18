from flask import Flask
import bookStore.books.book

def create_app():
    app = Flask('bookStore', static_folder=None)
    return app



