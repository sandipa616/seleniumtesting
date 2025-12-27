from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.maximize_window()
url="https://the-internet.herokuapp.com/drag_and_drop"
browser.get(url)
source_element=browser.find_element(By.ID,"column-a")
destination_element=browser.find_element(By.ID,"column-b")
action=ActionChains(browser)
action.drag_and_drop(source_element,destination_element).perform()
time.sleep(3)
action.drag_and_drop(destination_element,source_element).perform()
time.sleep(3)