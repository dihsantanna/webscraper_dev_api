from flask.testing import FlaskClient
from pytest import fixture
from webscraper_api.api.app import create_app

MONGODB_TEST_URI = "mongodb://localhost:27017/webscraper_test"


@fixture
def client_test() -> FlaskClient:
    """Create a test client."""
    app = create_app(MONGODB_TEST_URI)
    app.config.update(TESTING=True)
    return app.test_client()
