from selenium import webdriver
driver=webdriver.Chrome()
import time
viewports=[(375,667),(430,932),(360,740),(540,720),(1280,800),(1024,600),(414,896),(390,844),(412,915),(768,1024)
           ,(820,1180)]
driver.get("https://google.com")
try:
     for width,height in viewports:
         driver.set_window_size(width,height)
         time.sleep(1)
finally:
     driver.close()
