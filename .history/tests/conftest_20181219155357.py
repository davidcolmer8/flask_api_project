from simpleApp.app import startApp

import pytest
@pytest.fixture
def app(request):
    app = startApp()
    return app