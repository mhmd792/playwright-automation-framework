import os
import pytest
from playwright.sync_api import Page, Browser
from dotenv import load_dotenv, find_dotenv
from pages.login_page import LoginPage

# Load the hidden variables from the .env file into memory
load_dotenv(find_dotenv())

# --- Fixture 1: Standard UI Login (Slow, used for testing UI flows) ---
@pytest.fixture
def logged_in_page(page: Page):
    print("\n[Setup]: Logging in via UI with secure credentials...")
    login_page = LoginPage(page)
    
    page.goto(os.getenv("BASE_URL"))
    login_page.login(os.getenv("SAUCE_USERNAME"), os.getenv("SAUCE_PASSWORD"))
    
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
        "value": os.getenv("SAUCE_USERNAME"),
        "url": os.getenv("BASE_URL")
    }])
    
    page = context.new_page()
    page.goto(f"{os.getenv('BASE_URL')}/inventory.html")
    
    yield page
    
    print("\n[Teardown]: Closing fast context.")
    context.close()
    