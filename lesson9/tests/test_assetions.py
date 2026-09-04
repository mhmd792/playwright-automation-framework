from playwright.sync_api import expect

def test_test_assertions(page):
    page.goto("https://www.saucedemo.com/")
    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#login-button")).to_be_visible()
    expect(page.locator("#user-name")).to_be_empty()
    expect(page.locator("#password")).to_be_empty()
    expect(page.locator("#login-button")).to_be_enabled()
    expect(page.locator("#login-button")).to_have_text("Login")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html", timeout=5000)
    error_message = page.locator("[data-test='error']")
    expect(error_message).not_to_be_visible()


page.locator("#password").fill("secret_food")
page.locator("#user-name").fill("555")

login_button = page.locator("#login-button")
login_button.click()