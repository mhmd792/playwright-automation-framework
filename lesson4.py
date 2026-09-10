api_calls = []

api_calls.append({
    "api_response": "success",
    "response_code": 200,
    "error": None,
})

api_calls.append({
    "api_response": "failed",
    "response_code": 404,
    "error": "no_connection",
})

api_calls.append({
    "data": "some data missing required fields"
})


def check_api_calls(api_calls):
    for api_call in api_calls:
        try:
            if api_call["api_response"] == "success":
                print(" pass API call successful with response code:", api_call["response_code"])
            else:
                print(" fail API call failed with error:", api_call["error"], "and response code:", api_call["response_code"])
        except KeyError as e:
            print(f"Error: Missing key in API call data - {e}")


for api_call in api_calls:
    print(api_call)

check_api_calls(api_calls)