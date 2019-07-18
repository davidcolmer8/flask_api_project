from bookStore.app import create_app

import pytest

@pytest.fixture
def app(request):
    app = create_app()
    return app