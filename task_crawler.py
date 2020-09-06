from selenium import webdriver 
import requests
from bs4 import BeautifulSoup
import pandas as pd 

url='http://www.mca.gov.in/mcafoportal/viewCompanyMasterData.do'
cin=['U40108HP1995PTC016183',
'U40101HP1997PTC020577',
'U70200TG2009PTC063770',
'U15332MH1996PTC099964']

def OpenLink():
    driver = webdriver.Chrome(executable_path=r'E:\Beautiful-soup\Driver\chromedriver.exe')
    driver.get(url)
    for data in cin:
        driver.find_elements_by_id('companyID').send_keys(data)
        
