
@pytest.fixture
def app():
    app = create_app(testing=True)
    return app