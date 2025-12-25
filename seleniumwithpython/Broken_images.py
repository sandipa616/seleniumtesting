import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()
images=browser.find_elements(By.TAG_NAME,"img")
broken_images=[]
for image in images:
    src=image.get_attribute("src")
    if src:
        response=requests.get(src,timeout=5,headers={'user-agent':'Mozilla/5.0'})
        if response.status_code != 200:
            broken_images.append(src)
            print("Broken image found")
if broken_images:
    print("\nList of broken images :")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No broken images found")
browser.quit()
