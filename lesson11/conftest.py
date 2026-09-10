import os
import sys
from pathlib import Path

import pytest
from playwright.sync_api import Page
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from login_page import LoginPage

load_dotenv()

@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(os.environ["SAUCE_USERNAME"], os.environ["SAUCE_PASSWORD"])
    return page