import pytest from app.app
import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_health(client):
    rv = client.get('/health')
    assert rv.get_json()['healthy'] == True

def test_home_returns_version(client):
    rv = client.get('/')
    data = rv.get_json()
    assert 'version' in data
    assert data['status'] == 'ok'


