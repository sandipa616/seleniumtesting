from selenium import webdriver
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('credential.json','r') as file:
    test_data=json.load(file)
for data in test_data:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(data['username'])
    driver.find_element(By.ID, "password").send_keys(data['password'])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    driver.quit()
