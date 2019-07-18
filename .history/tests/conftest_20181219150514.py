import json
import pytest

from simpleApp.app import startApp

@py
def app():
    app = startApp(testing=True)
    return app