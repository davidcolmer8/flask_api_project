from flask import Flask
import bookbooks.book

def create_app():
    app = Flask('bookStore')
    return app



