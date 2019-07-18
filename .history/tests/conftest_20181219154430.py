from simpleApp.app import startApp

@pytest.fixture
def app():
    appaa = startApp()
    return app