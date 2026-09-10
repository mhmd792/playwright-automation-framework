import pytest
from playwright.sync_api import Page

from pages.inventory_page import InventoryPage


@pytest.mark.smoke
@pytest.mark.regression
def test_sort_name_a_to_z(api_logged_in_page: Page):
    """TC-INV-001: Products are sorted alphabetically ascending by name."""
    inventory_page = InventoryPage(api_logged_in_page)

    inventory_page.sort_by(InventoryPage.SORT_NAME_A_TO_Z)

    names = inventory_page.get_product_names()
    assert names == sorted(names), f"Names are not sorted A to Z: {names}"


@pytest.mark.smoke
@pytest.mark.regression
def test_sort_price_low_to_high(api_logged_in_page: Page):
    """TC-INV-002: Products are sorted by price ascending."""
    inventory_page = InventoryPage(api_logged_in_page)

    inventory_page.sort_by(InventoryPage.SORT_PRICE_LOW_TO_HIGH)

    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices), f"Prices are not sorted low to high: {prices}"


@pytest.mark.smoke
@pytest.mark.regression
def test_cart_badge_shows_two_after_adding_two_items(api_logged_in_page: Page):
    """TC-CART-001: The cart badge reflects the number of added items."""
    inventory_page = InventoryPage(api_logged_in_page)

    inventory_page.add_items_to_cart(2)

    inventory_page.expect_cart_badge_count(2)


@pytest.mark.regression
def test_sorted_by_price_then_add_two_items(api_logged_in_page: Page):
    """TC-INV-003: Sorting is preserved and the cart badge updates correctly."""
    inventory_page = InventoryPage(api_logged_in_page)

    inventory_page.sort_by(InventoryPage.SORT_PRICE_LOW_TO_HIGH)
    prices = inventory_page.get_product_prices()
    assert prices == sorted(prices), f"Prices are not sorted low to high: {prices}"

    inventory_page.add_items_to_cart(2)

    inventory_page.expect_cart_badge_count(2)