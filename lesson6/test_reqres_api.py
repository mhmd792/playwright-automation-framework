import pytest
import requests

@pytest.fixture
def headers():
    return {
        "x-api-key": "free_user_3HyKbRIqwAvbfox8wusLJtkMSSs"
    }

@pytest.fixture
def body():
    return {
        "name": "morpheus",
        "job": "leader"
    }

def test_single_user(headers):
    print("--- Testing GET Request ---")
    get_url = "https://reqres.in/api/users/3"

    response = requests.get(get_url, headers=headers)
    json_response = response.json()
    print(json_response["data"]["first_name"])

    assert response.status_code == 200
    assert json_response["data"]["id"] == 3
    assert json_response["data"]["first_name"] == "Emma"
    assert "id" in json_response["data"]


def test_get_user(headers):
    print("--- Testing GET Request for user 3 ---")
    get_url = "https://reqres.in/api/users/3"

    response = requests.get(get_url, headers=headers)
    json_response = response.json()
    print(json_response["data"]["first_name"])

    assert response.status_code == 200
    assert json_response["data"]["id"] == 3
    assert "first_name" in json_response["data"]


def test_create_user(headers, body):
    print("--- Testing POST Request ---")
    post_url = "https://reqres.in/api/users"

    response = requests.post(post_url, headers=headers, json=body)
    json_response = response.json()
    print(json_response)

    assert response.status_code == 201
    assert json_response["name"] == body["name"]
    assert json_response["job"] == body["job"]
    assert "id" in json_response
    assert "createdAt" in json_response



