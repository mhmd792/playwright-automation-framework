import requests

print("--- Testing GET Request ---")
get_url = "https://reqres.in/api/users/2"
headers = {
    "x-api-key": "free_user_3HyKbRIqwAvbfox8wusLJtkMSSs"
}
response = requests.get(get_url, headers=headers)
json_response = response.json()
print(json_response["data"]["first_name"])


print("--- Testing POST Request ---")
post_url = "https://reqres.in/api/users"

my_payload = {
    "name": "John Doe",
    "job": "Software Engineer"
}
post_response = requests.post(post_url, headers=headers, json=my_payload)
print(post_response.status_code)
response_data = post_response.json()
print(response_data)
