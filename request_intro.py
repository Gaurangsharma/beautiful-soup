import requests
from bs4 import BeautifulSoup
import pandas as pd
wiki_link="https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Asia"
link=requests.get(wiki_link).text
soup=BeautifulSoup(link,'html.parser')
right_table=soup.find(class_='wikitable sortable')
table_link=right_table.find_all('a')
data_link=[]
for data in table_link:
    data_link.append(data.get("title"))
country=[]
for i in data_link:
    temp=True
    if i!=None:
        check_list=list(map(str,i.split(" ")))
        if "language" in check_list or "Flag" in check_list:
            temp=False
        if temp:
            country.append(i) 
dup=set(country)
country=list(dup)
df=pd.DataFrame()
df['country']=country
df['fdsec']=dup
print(df)