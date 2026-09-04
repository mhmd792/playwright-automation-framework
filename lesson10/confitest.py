import pytest
from playwright.sync_api import Page
from pages.login_page import login_page

@pytest.fixture
def login_page_fixture(page: Page):
    login_page=LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    yield page
    login_page.close()