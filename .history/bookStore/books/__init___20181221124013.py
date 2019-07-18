from flask import Flask

app = Flask('bookStores', static_folder=None)

import bookStore.books