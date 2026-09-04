from playwright.sync_api import Page, expect

from pages.inventorey_page import inventory_page
from pages.login_page import login_page



def test_add_itam_to_cart(page: Page):
    login_page = loginPage(page)
    inventory_page = inventory_page(page)


    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_backpack()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1", timeout=3000)
    