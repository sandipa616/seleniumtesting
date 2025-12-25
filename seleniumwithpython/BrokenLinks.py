import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
all_links=driver.find_elements(By.TAG_NAME,'a')
broken_count=0
for link in all_links:
  href=link.get_attribute("href")
  try:
    response = requests.get(href, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code >= 400:
        print(f"Broken link: {href} (status code: {response.status_code})")
        broken_count+=1
  except requests.exceptions.RequestException:
   print("Request failed")
print(f"Broken links: {broken_count}")
print(f"Total number of link on page:{len(all_links)}")
time.sleep(1)
