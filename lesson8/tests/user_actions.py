import time
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    page.locator('#user-name').fill("standard_user")
    page.locator("#password").fill("secure_sauce")
    page.locator("#login-button").click()

    time.sleep(2)
    browser.close()
