
def test_api_home(client):
    resp = client.get('/api-v1/')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['api_version'] == '1.0'
    assert 'db_users' in data
