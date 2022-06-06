import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari() 

# define URL
URL = 'https://housestockwatcher.com/summary_by_rep'
driver.implicitly_wait(20)
driver.get(URL)
print(driver.title)

search = driver.find_element(by= By.TAG_NAME, value="input")
search.send_keys("nancy pelosi")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(20)
search2 = driver.find_element(by=By.LINK_TEXT, value="View Summary").click()

tables = driver.find_element(by=By.TAG_NAME, value="table")
tables.getText()



time.sleep(8)
driver.quit()