from selenium import webdriver
from datetime import datetime,timedelta

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
url="https://www.globalsqa.com/demo-site/datepicker/#Icon%20Trigger"
driver.get(url)
driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//a[@class='close_img']").click()
frame=driver.find_element(By.XPATH,"//div[@class='single_tab_div resp-tab-content resp-tab-content-active']//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#datepicker").click()
current_date=datetime.now()
next_date =current_date + timedelta(days=-2)
formatted_date=next_date.strftime("%m/%d/%y")
driver.find_element(By.CSS_SELECTOR,"#datepicker").send_keys(formatted_date+Keys.TAB)
time.sleep(5)
driver.quit()