from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.selenium.dev/")
time.sleep(1)
browser.switch_to.new_window()
browser.get("https://playwright.dev/")
number_of_tabs=len(browser.window_handles)
print(number_of_tabs)
tabs_value=browser.window_handles
print(tabs_value)
current_tab=browser.current_window_handle
print(current_tab)
parent_tab=browser.window_handles[0]
print(parent_tab)
browser.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()
time.sleep(2)
if current_tab!=parent_tab:
    browser.switch_to.window(parent_tab)
browser.find_element(By.XPATH,"//span[normalize-space()='Downloads']").click()
time.sleep(5)


