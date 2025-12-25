from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.execute_script("window.scrollTo(0,700)")
table=driver.find_element(By.ID,"countries")
rows=table.find_elements(By.TAG_NAME,"tr")
rows_count=len(rows)-1
print(rows_count)
target_value="Nepal"
found=False
for row in rows:
    cells=row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found value: {target_value}")
            found=True
            break
    if found:
        break
if not found:
    print(f"{target_value} not found")

time.sleep(5)
