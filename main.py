import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Safari() 

# define URL
URL = 'https://housestockwatcher.com/summary_by_rep'
driver.implicitly_wait(20)
driver.get(URL)
driver.maximize_window()
print(driver.title)

search = driver.find_element(by= By.TAG_NAME, value="input")
search.send_keys("nancy pelosi")
search.send_keys(Keys.RETURN)

driver.implicitly_wait(20)
search = driver.find_element(by=By.LINK_TEXT, value="View Summary").click()


#stops working here, no such element exception trying to find ANY element
text = driver.find_elements(by=By.XPATH, value="//table[@class= 'items-center w-full bg-transparent']/tbody/tr")

time.sleep(8)
driver.quit()