from flask import Flask

def create_app():
    app = Flask('bookStore')
    
    return app.run()
import books.book


