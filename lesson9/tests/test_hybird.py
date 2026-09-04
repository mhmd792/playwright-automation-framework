from playwright.sync_api import expect

def test_test_hybird(page):
    response = page.request.get("https://jsonplaceholder.typicode.com/posts /1")

    expect(response).to_be_ok()

    api_title = response.json()["title"]
    print(f"API title: {api_title}")

page.goto("https://www.saucedemo.com/")
expect(page).to_have_title("Swag Labs")
expect(page.locator("#login-button")).to_be_visible()