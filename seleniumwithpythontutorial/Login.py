from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
username="standard_user"
password="secret_sauce"
login_url="https://www.saucedemo.com/"
driver.get(login_url)
username_field=driver.find_element(By.ID,"user-name")
password_field=driver.find_element(By.ID, "password")
username_field.send_keys(username)
password_field.send_keys(password)
login_button=driver.find_element(By.ID,"login-button")
assert login_button.is_enabled()
login_button.click()
success_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "title"))
)
assert success_element.text=="Products"
time.sleep(5)