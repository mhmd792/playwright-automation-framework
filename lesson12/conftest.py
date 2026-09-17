import os
import pytest
from playwright.sync_api import Page, Browser
from dotenv import load_dotenv, find_dotenv
from pages.login_page import LoginPage

# Load the hidden variables from the .env file into memory
load_dotenv(find_dotenv())

BASE_URL = os.getenv("BASE_URL") or "https://www.saucedemo.com/"
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME") or "standard_user"
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD") or "secret_sauce"

# --- Fixture 1: Standard UI Login (Slow, used for testing UI flows) ---
@pytest.fixture
def logged_in_page(page: Page):
    print("\n[Setup]: Logging in via UI with secure credentials...")
    login_page = LoginPage(page)
    
    page.goto(BASE_URL)
    login_page.login(SAUCE_USERNAME, SAUCE_PASSWORD)
    
    yield page  
    
    print("\n[Teardown]: Closing browser safely.")


# --- Fixture 2: API Login Injection (Fast, used to skip UI Login) ---
@pytest.fixture
def api_logged_in_page(browser: Browser):
    print("\n[Setup]: Fast API Login using Cookie Injection...")
    
    context = browser.new_context()
    
    # Inject the authentication cookie to bypass the UI login screen
    context.add_cookies([{
        "name": "session-username",
        "value": SAUCE_USERNAME,
        "url": BASE_URL
    }])
    
    page = context.new_page()
    page.goto(f"{BASE_URL.rstrip('/')}/inventory.html")
    
    yield page
    
    print("\n[Teardown]: Closing fast context.")
    context.close()
    