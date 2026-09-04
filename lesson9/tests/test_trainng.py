from playwright.sync_api import sync_playwright

def test_playwright_get():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")

        parsed_get_data = get_response.json()
        assert get_response.status == 200

       
        assert parsed_get_data['id'] == 1
        assert "title" in parsed_get_data
        browser.close()


def test_playwright_post():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = "https://jsonplaceholder.typicode.com/posts"
        data = {
            "title": "do not delete",
            "body": "bar",
            "userId": 200
        }
        post_response = page.request.post(url, data=data)

        parsed_post_data = post_response.json()
        assert post_response.status == 201

        assert parsed_post_data['title'] == "do not delete"
        assert parsed_post_data['body'] == "bar"
        assert parsed_post_data['userId'] == 200
        browser.close()        



    