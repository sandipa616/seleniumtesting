from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
username="admin"
password="admin"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
#https://username:password@domain/path