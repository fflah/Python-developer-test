import pytest

@pytest.fixture
def test_app():
    from app import app

    return app

@pytest.fixture
def client(test_app):
    return test_app.test_client()
    