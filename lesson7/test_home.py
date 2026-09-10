import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver


def test_successful_login(logged_in_driver):
    assert "inventory.html" in logged_in_driver.current_url, "login failed, url did not change"


def test_add_to_cart(logged_in_driver):
    logged_in_driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    cart_badge = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_badge.text == "1", "item was not added to the cart"

    logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = logged_in_driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert cart_item.text == "Sauce Labs Backpack", "wrong item in cart"

