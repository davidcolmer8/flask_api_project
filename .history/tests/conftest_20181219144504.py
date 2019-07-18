import json
import pytest

from simpleApp.app import startApp

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app