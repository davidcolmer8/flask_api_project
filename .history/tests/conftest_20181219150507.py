import json
import pytest

from simpleApp.app import startApp

def app():
    app = startApp(testing=True)
    return app