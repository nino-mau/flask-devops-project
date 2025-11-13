import app

def test_home_page(client):
    """Test que la page d'accueil fonctionne"""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200