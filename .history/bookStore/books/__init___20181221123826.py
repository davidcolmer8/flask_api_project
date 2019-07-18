from flask import Flask

app = Flask('bookStore', static_folder=None)

import bookStorebooks.book