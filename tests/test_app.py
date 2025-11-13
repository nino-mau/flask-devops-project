"""Tests for Flask application routes"""


def test_home_page(client):
    """Test that the home page works correctly"""
    response = client.get('/')
    assert response.status_code == 200



