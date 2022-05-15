from http import HTTPStatus
from api.tests.conftest import fake_scanned_info


def test_get_token(api_client, test_user):
    response = api_client.post(
        "/api/token/", {"username": test_user.username, "password": "test"}
    )
    assert response.status_code == 200
    assert response.data["token"]
    assert response.data["user"]
    assert response.data["user"]["username"] == test_user.username


def port_scanner(api_client, test_user):
    data = {
        "target": "thewatchcode.com",
        "port_range": "1-1024",
        "command": "--script=dns-brute",
    }
    response = api_client.post("/api/portscanner/", data)
    assert response.status_code == 200


def test_retrieve_weather_using_mocks(mocker, fake_scanned_info):

    # Creates a fake requests response object
    fake_resp = mocker.Mock()
    # Mock the json method to return the static weather data
    fake_resp.json = mocker.Mock(return_value=fake_scanned_info)
    # Mock the status code
    fake_resp.status_code = HTTPStatus.OK

    