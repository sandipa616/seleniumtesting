from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
dropdown=driver.find_element(By.ID,"city")
target_value="Meerut"
select=Select(dropdown)
for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
    else:
        print(f"{target_value} not found in dropdown")

# option_count=len(select.options)
# expected_count=4
# if option_count==expected_count:
#     print("Test Passed,Count is correct")
# else:
#     print("Test Failed,Count is incorrect")
# #select the value by visible text
# #select the value by Index
# #select the option by using a value
# # select.select_by_value("Agra")
# # select.select_by_index(3)
time.sleep(5)