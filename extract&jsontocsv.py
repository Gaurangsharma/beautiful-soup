# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# link=requests.get("https://www.allrecipes.com/").text
# soup=BeautifulSoup(link,'html.parser')
# data_container=soup.find_all(class_='recipeCard__imageLink',href=True,limit=10)
# href=[item['href'] for item in data_container]

# Recipi_id,ingrediant_section,cooking_instruction=[],[],[]
# for url in href:
#     linkk=requests.get(url).text
#     soupp=BeautifulSoup(linkk,'html5lib')
#     data=soupp.find(class_="recipe-summary")
#     data2=soupp.find(id="lst_ingredients_1")
#     data3=soupp.find(id="lst_ingredients_2")
#     recipe_directions =soupp.find(class_="directions--section") 

#     Recipe_ID=data.find('h1',class_="recipe-summary__h1") 
#     if(Recipe_ID):
#         Recipi_id.append(Recipe_ID.get_text())
#         author=data2.find_all(class_="recipe-ingred_txt")
#         author2=data3.find_all(class_="recipe-ingred_txt")
#         ind=[]
#         for i in author:
#             ind.append(i.get_text())
#         for i in author2:
#             ind.append(i.get_text())

#         ingrediant_section.append(ind)
#         dire=[]
#         direction=recipe_directions.find_all(class_="recipe-directions__list--item") 
#         for i in direction:
#             dire.append((i.get_text()).strip())
#         cooking_instruction.append(dire)
# df=pd.DataFrame(
#     {
#     'Recipe_ID':Recipi_id,
#     'Ingredient_Section':ingrediant_section,
#     'Cooking_Instructions':cooking_instruction
#     })
# df.to_json('recipe.json')
# df.to_csv('recipe.csv')
