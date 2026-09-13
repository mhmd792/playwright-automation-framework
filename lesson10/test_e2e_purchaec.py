from playwright.sync_api import Page, expect

from inventorey_page import inventory_page
from login_page import LoginPage


def test_add_itam_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory = inventory_page(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory.add_backpack_to_cart()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1", timeout=3000)
