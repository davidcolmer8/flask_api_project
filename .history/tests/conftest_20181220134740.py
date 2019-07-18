from bookStore.app import starcreate_apptApp

import pytest

@pytest.fixture
def app(request):
    app = startApp()
    return app