from flask import Flask

def create_app():
    app = Flask('bookStore')
    
    return app
import bookstore.books.book


