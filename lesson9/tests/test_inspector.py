

def test_inspector(page):
    page.goto("https://www.saucedemo.com/")
    
    page.pause()

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    
    page.locator("#login-button").click()

