from simpleApp.app import startApp

@pytest.fixture
def app(request):
    app = startApp()
    return app