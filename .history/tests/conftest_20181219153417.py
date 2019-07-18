import json
import pytest

from simpleApp.app import startApp

@py////////test.fixture
def app():
    app = startApp()
    return app