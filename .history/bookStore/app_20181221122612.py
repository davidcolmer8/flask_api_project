from flask import Flask

app = Flask('bookStore', static_folder=None)

import books.book

