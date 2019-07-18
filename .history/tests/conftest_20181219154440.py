from simpleApp.app import startApp

@pytest.fixture
def app():
    app = startApp()
    return app