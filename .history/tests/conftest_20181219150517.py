import json
import pytest

from simpleApp.app import startApp

@pytest.
def app():
    app = startApp(testing=True)
    return app