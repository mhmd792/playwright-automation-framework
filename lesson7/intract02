import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

username_box=driver.find_element(By.ID, "username")
password_box=driver.find_element(By.ID, "password")
login_button=driver.find_element(By.CLASS_NAME, "radius")


username_box.send_keys("tomsmith")

my_password="SuperSecretPassword!"
password_box.send_keys(my_password)

login_button.click()
time.sleep(10)
driver.quit()


