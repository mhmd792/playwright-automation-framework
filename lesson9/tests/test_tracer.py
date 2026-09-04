from playwright.sync_api import expect, sync_playwright

def test_tracer():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()

        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("555")

        btn = page.locator("#login-button")
        btn.click()

        

        try:
            expect(page.locator("title")).to_have_text("products",timeout=2000)
        finally:
                context.tracing.stop(path="trace.zip")
                browser.close()

                