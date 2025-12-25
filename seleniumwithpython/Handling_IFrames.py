from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
iframe=driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)
Text_Editor=driver.find_element(By.ID,"tinymce")
Text_Editor.send_keys(Keys.CONTROL + "a")  # select all
Text_Editor.send_keys(Keys.BACKSPACE)      # delete
Text_Editor.send_keys("Hello I am Sandipa and Currently I am learning selenium automation testing with python")
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']").click()
time.sleep(10)