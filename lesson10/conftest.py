import pytest
from playwright.sync_api import Page

from login_page import LoginPage


@pytest.fixture
def login_page_fixture(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    yield page


@pytest.fixture
def logged_in_page(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    return page
