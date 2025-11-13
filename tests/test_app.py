"""Tests for Flask application routes"""


def test_home_page(client):
    """Test that the home page works correctly"""
    response = client.get("/")
    assert response.status_code == 200


def test_videos_page(client):
    """Test that the videos page works correctly"""
    response = client.get("/videos")
    assert response.status_code == 200


def test_add_video_page(client):
    """Test that the add_video page works correctly"""
    response = client.get("/videos/add")
    assert response.status_code == 200
