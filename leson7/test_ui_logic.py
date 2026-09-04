from selenium import webdriver 
from selenium.webdriver.common.by import By 

def test_successful_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    username_box = driver.find_element(By.ID, "user-name")
    password_box = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_box.send_keys("standard_user")
    my_password = "secret_sauce"
    password_box.send_keys(my_password)

    login_button.click()
    
    # Add assertions here to verify successful login
    assert "inventory.html" in driver.current_url,"login failed,url dont change"

    driver.quit()

