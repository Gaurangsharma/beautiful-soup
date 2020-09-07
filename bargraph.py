import requests
from bs4 import BeautifulSoup
import pandas as pd 
from matplotlib import pyplot as plt 

# from selenium import webdriver


# def get_value(url):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     driver.find_element_by_id('bt_gerar_cpf').click()
#     while driver.find_element_by_id('texto_cpf').text == 'Gerando...':
#         continue

link=requests.get("https://www.allrecipes.com/recipes/86/world-cuisine/").text
soup=BeautifulSoup(link,'html.parser')

data_container=soup.find_all(class_="carouselNav__link recipeCarousel__link",href=True,limit=7)

href=[item['href'] for item in data_container]
cuisine_name=[(item.find(class_="carouselNav__linkText").get_text()).strip() for item in data_container]

print(href)
print(cuisine_name)
dishes_count=[]
for i in href:
    linkk=requests.get(i).text
    soupp=BeautifulSoup(linkk,'html.parser')
    cuisine_data=soupp.find_all(class_="recipeCard")
    dishes_count.append(len(cuisine_data))

print(dishes_count)
plt.bar(cuisine_name, dishes_count, color ='maroon',  
        width = 0.4) 
  
plt.xlabel("Cusine Name") 
plt.ylabel("No. of dishes") 
plt.title("Cusine Details") 
plt.show() 