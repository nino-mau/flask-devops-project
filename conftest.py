import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """Fixture for Flask application"""
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app


@pytest.fixture
def client(app):
    """Fixture for Flask test client"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Fixture for Flask CLI runner"""
    return app.test_cli_runner()
