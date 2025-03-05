import pytest
import requests
from lesson_24.test_task_1 import BASE_URL
from requests.auth import HTTPBasicAuth


@pytest.fixture(scope='session')
def auth_token():
    auth_data = ('test_user', 'test_pass')
    response = requests.post(f"{BASE_URL}/auth", auth=requests.auth.HTTPBasicAuth(*auth_data))
    token = response.json().get('access_token')

    assert response.status_code == 200, 'Token not received'

    return token
