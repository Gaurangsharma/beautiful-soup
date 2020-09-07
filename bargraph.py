# import json
# from matplotlib import pyplot as plt

# f=open('train.json')
# data=json.load(f)
# cuisine_name, dishes_count=[],[]
# for i in range(len(data)):
#     cuisine_name.append(data[i]['cuisine'])
#     dishes_count.append(len(data[i]['ingredients']))
# bar_graph(cuisine_name,dishes_count)


def bar_graph(cuisine_name,dishes_count):
    plt.bar(cuisine_name, dishes_count, color ='maroon',  
            width = 0.4) 
    
    plt.xlabel("Cusine Name") 
    plt.ylabel("No. of dishes") 
    plt.title("Cusine Details") 
    plt.show() 



import requests
from bs4 import BeautifulSoup
import pandas as pd 
from matplotlib import pyplot as plt 
import json

link=requests.get("https://www.allrecipes.com/recipes/86/world-cuisine/").text
soup=BeautifulSoup(link,'html.parser')

data_container=soup.find_all(class_="carouselNav__link recipeCarousel__link",href=True,limit=2)

href=[item['href'] for item in data_container]
cuisine_name=[(item.find(class_="carouselNav__linkText").get_text()).strip() for item in data_container]

print(href)
print(cuisine_name)
dishes_count=[]
for i in href:
    linkk=requests.get(i).text
    soupp=BeautifulSoup(linkk,'html.parser')
    j=110
    while(1):
        print(j)
        new_link=i+"?page="+str(j)
        linkkk=requests.get(new_link).text
        souppp=BeautifulSoup(linkkk,'html.parser')
        btn=souppp.find(class_="category-page-list-related-nav-next-button")
        if(btn):
            j+=1
        else:
            cnt=souppp.find_all(class_="recipeCard")
            break
    count=36+(j-1)*24+len(cnt)
    dishes_count.append(count)
bar_graph(cuisine_name,dishes_count)

# print(dishes_count)
