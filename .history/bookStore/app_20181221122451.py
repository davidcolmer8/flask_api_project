from flask import Flask

    app = Flask('bookStore', static_folder=None)
    return app


import books.book
