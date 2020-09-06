from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://gstatic.com/")

driver.find_elements_by_name('username').send_keys('gaurang.sharma_cs16')
driver.find_elements_by_id('ft_pd').send_keys('55800469')
driver.find_elements_by_link_text('Continue').click()
time.sleep(15)
driver.quit()