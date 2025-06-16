from createflaskapp import app, db
from createflaskapp.models import User


def test_user_registration_and_login(client):
    # Register a new user
    resp = client.post('/auth/register', data={
        'username': 'testuser',
        'first_name': 'Test',
        'last_name': 'User',
        'email_address': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=False)
    assert resp.status_code == 302
    assert '/auth/login' in resp.headers['Location']

    # User should exist in the database
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None

    # Login with created user
    resp = client.post('/auth/login', data={
        'email_address': 'test@example.com',
        'password': 'password123'
    }, follow_redirects=False)
    assert resp.status_code == 302
    assert resp.headers['Location'].endswith('/')
