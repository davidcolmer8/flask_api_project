import json
import pytest

from simpleApp.app import startApp

@pytest.fixtures
def app():
    app = startApp(testing=True)
    return app