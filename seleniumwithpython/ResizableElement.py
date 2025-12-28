from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.maximize_window()
url="https://demo.automationtesting.in/Resizable.html"
browser.get(url)
resizable_element=browser.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_element_size=browser.find_element(By.XPATH,"//div[@id='resizable']")
initial_size=initial_element_size.size
print("Initial size",initial_size)
time.sleep(5)
action=ActionChains(browser)
action.click_and_hold(resizable_element).move_by_offset(100,100).release().perform()
time.sleep(5)
resized_element=initial_element_size.size
print("Resized size",resized_element)
time.sleep(5)
browser.quit()