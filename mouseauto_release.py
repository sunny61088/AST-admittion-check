from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:\SunnyFiles\chromedriver.exe")
driver.get("http://fast.uac.edu.tw/INSERT")
#insert ID
sleep(2)
driver.save_screenshot('screenshot.png')