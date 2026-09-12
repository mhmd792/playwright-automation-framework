
import requests

print("--- Testing GET Request ---")
def test_get_request():
    get_url = "https://reqres.in/api/users/2"
    headers = {
        "x-api-key": "free_user_3HyKbRIqwAvbfox8wusLJtkMSSs"
    }

    response = requests.get(get_url, headers=headers)
    json_response = response.json()
    print(json_response["data"]["first_name"])

    assert response.status_code == 200

    assert json_response["data"]["id"] == 2
    assert json_response["data"]["first_name"] == "janet"



def test_post_request():
    print("--- Testing POST Request ---")
    post_url = "https://reqres.in/api/users"
    headers = {
        "x-api-key": "free_user_3HyKbRIqwAvbfox8wusLJtkMSSs"
    }
    payload = {
        "name": "mohammad",
        "job": "gamer"
    }

    response = requests.post(post_url, headers=headers, json=payload)
    json_response = response.json()
    print(json_response)
    
    assert response.status_code == 201
    assert json_response["name"] == "mohammad"
    assert json_response["job"] == "gamer"
    assert "id" in json_response


