import json
import pytest

from simpleApp.app import startApp

@pytest.fixture
def app():
    app = startApp()
    return app