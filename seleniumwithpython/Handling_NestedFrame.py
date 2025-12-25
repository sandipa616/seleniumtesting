from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")
#Switching to top frame
driver.switch_to.frame("frame-top")
#Switching to middle frame
driver.switch_to.frame("frame-left")
content_left=driver.find_element(By.TAG_NAME,"body").text
print(f"The content in Left Frame: {content_left}")
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
content_bottom=driver.find_element(By.TAG_NAME,"body").text
print(f"The content in Bottom Frame: {content_bottom}")
time.sleep(2)