from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
checkboxes=driver.find_elements(By.XPATH,"(//input[@type='checkbox'])")
for checkbox in checkboxes:
    if checkbox.is_selected():  # if checked, uncheck
        driver.execute_script("arguments[0].click();", checkbox)
    else:                      # if unchecked, check
        driver.execute_script("arguments[0].click();", checkbox)
checked_count=0
for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count+=1
expected_checked_count=3
if expected_checked_count == checked_count:
    print("checkbox count verified")
else:
    print("checkbox count mismatched")
time.sleep(5)
driver.close()