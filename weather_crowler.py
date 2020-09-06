import requests
from bs4 import BeautifulSoup
import pandas as pd

link=requests.get("https://forecast.weather.gov/MapClick.php?lat=39.39870315600007&lon=-99.41461918999994").text
soup=BeautifulSoup(link,'html.parser')
data_container=soup.find_all(class_='tombstone-container')

period_name=[item.find('p',class_="period-name").get_text() for item in data_container]
short_desc=[item.find('p',class_="short-desc").get_text() for item in data_container]
temp=[item.find('p',class_="temp").get_text() for item in data_container]

        df=pd.DataFrame(
    {
    'period_name':period_name,
    'short_desc':short_desc,
    'temp':temp
    })
print(df)
df.to_csv('weather.csv')


# from selenium import webdriver
# import time
# browser=webdriver.Chrome()
# browser.get('http://google.com/')
# time.sleep('5')
# browser.quit()