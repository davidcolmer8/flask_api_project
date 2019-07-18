from simpleApp.app import startApp

@py/.fixture
def app():
    app = startApp()
    return app