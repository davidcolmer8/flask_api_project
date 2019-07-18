from flask import Flask
import books.book

def create_app():
    app = Flask('bookStore')
    return app



