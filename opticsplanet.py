from mailbox import Babyl
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Safari() 

# define URL
URL = 'https://opticsplanet.com/'
driver.implicitly_wait(20)
driver.get(URL)
driver.maximize_window()
print(driver.title)

products = driver.find_element(by=By.ID, value="home-page-contents")
print(products.text)

products = driver.find_elements(by=By.CLASS_NAME, value="grid_link")
print(f"Number of products on home page are {len(products)}")

products = driver.find_elements(by=By.XPATH, value="//*[@id='home-page-contents']/div[1]/div[2]/div[2]/div/div/a")
for prices in products:
    print(prices.text)