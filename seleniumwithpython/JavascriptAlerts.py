from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# ---------- JS ALERT ----------
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("JS Alert text:", alert.text)
time.sleep(1)
alert.accept()

result = driver.find_element(By.ID, "result").text
print("Result:", result)
time.sleep(2)
# ---------- JS CONFIRM ----------
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert = driver.switch_to.alert
print("JS Confirm text:", alert.text)
time.sleep(1)
alert.dismiss()   # Cancel
# alert.accept()  # OK

result = driver.find_element(By.ID, "result").text
print("Result:", result)
time.sleep(2)
# ---------- JS PROMPT ----------
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert = driver.switch_to.alert
print("JS Prompt text:", alert.text)
alert.send_keys("Selenium Test done by Sandipa")
time.sleep(1)
alert.accept()

result = driver.find_element(By.ID, "result").text
print("Result:", result)
time.sleep(3)
driver.quit()
