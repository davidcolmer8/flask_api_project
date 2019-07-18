from flask import Flask

app = Flask('bookStore', static_folder=None)

from blah import app

app.run(debug=True)

