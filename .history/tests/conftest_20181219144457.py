import json
import pytest

from simp.app import create_app

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app