from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print(page.title())

    page.locator('#user-name').fill("standard_user")
    page.locator('#password').fill("secret_sauce")
    page.locator('#login-button').click()

    page.get_by_role("listitem").filter(has_text="Sauce Labs Backpack").get_by_role("button", name="Add to cart").click()
    expect(page.locator("#shopping_cart")).to_have_text("1")

    product_name = "Sauce Labs Backpack"
    print(f"'{product_name}' has been added to the cart.")

#i know that i must to make the check for the url by assert but i think that the expect is more short in this line .
expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


browser.close()
