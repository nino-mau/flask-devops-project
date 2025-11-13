"""Tests for video-related routes"""


def test_videos_page(client):
    """Test that the videos page works correctly"""
    response = client.get("/videos")
    assert response.status_code == 200
