import json
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

option = webdriver.ChromeOptions()
preference={}'download.default_directory':"E:\Beautiful-soup\Driver",'safebrowsing-enablesd':'false'}
option.add_experimental_options('prefs',preference)
driver=webdriver.Chrome(chrome_options=option)
driver.get("http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do").content

driver.find_element_by_xpath()