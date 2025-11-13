import app

#Tests page /videos
def test_videos_page(client):
    """Test que la page d'accueil fonctionne"""
    client = app.test_client()
    response = client.get('/videos')
    assert response.status_code == 200



