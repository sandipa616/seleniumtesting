from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Datepicker.html")

driver.find_element(By.ID, "datepicker2").click()
time.sleep(2)

current_date = datetime.now()

# Month index (0–11)
current_month = current_date.month - 1

# %12 logic
next_month = (current_month + 1) % 12

# Year rollover
next_year = current_date.year + 1 if next_month == 0 else current_date.year

# Select month by INDEX ✅
month_dropdown = Select(
    driver.find_element(By.CSS_SELECTOR, "select[title='Change the month']")
)
month_dropdown.select_by_index(next_month)

# Select year by visible text
year_dropdown = Select(
    driver.find_element(By.CSS_SELECTOR, "select[title='Change the year']")
)
year_dropdown.select_by_visible_text(str(next_year))
target_day=current_date+timedelta(days=1)
driver.find_element(By.LINK_TEXT,str(target_day.day)).click()
time.sleep(5)
