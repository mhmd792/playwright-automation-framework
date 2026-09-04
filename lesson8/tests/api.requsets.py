
from playwright.sync_api import sync_playwright  # type: ignore[reportMissingImports]
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    

    get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"status code: {get_response.status}")
    parsed_get_data = get_response.json()
    print(f"retrieved title: {parsed_get_data['title']}\n")

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 100
    }
    post_response = page.request.post(url, data=data)
    print(f"status code: {post_response.status}")
    parsed_post_data = post_response.json()
    print(f"ID is: {parsed_post_data['id']}")
    print(f"Title is: {parsed_post_data['title']}")






    