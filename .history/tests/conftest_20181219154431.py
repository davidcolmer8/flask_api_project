from simpleApp.app import startApp

@pytest.fixture
def app():
    appa = startApp()
    return app