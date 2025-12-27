from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
browser=webdriver.Chrome()
browser.maximize_window()
url="https://demo.automationtesting.in/Datepicker.html"
browser.get(url)
actions = ActionChains(browser)
hover_element=browser.find_element(By.XPATH,"//a[normalize-space()='SwitchTo']")
time.sleep(5)
actions.move_to_element(hover_element).perform()
time.sleep(3)
browser.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()
time.sleep(5)
