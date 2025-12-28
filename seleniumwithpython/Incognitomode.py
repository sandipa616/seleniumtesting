import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.com/")
time.sleep(5)