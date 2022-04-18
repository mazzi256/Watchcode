import json
from xmlrpc import client
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username="test", password="test")
    return user


@pytest.fixture
def api_client(test_user):
    client = APIClient()
    client.login(test_user)
    return client

@pytest.fixture()
def fake_scanned_info():
    """Fixture that returns a scanned data."""
    with open("api/tests/resources/port_scanner_data.json") as f:
        return json.load(f)
