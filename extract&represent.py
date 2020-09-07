import requests
from bs4 import BeautifulSoup


def print_output(ind,dire):
    print('____'*15+"RECIPE"+'____'*15)

    print()
    print("INGREDIENT SECTION")
    print()
    for ingr in range(len(ind)-1):
        print(ind[ingr])

    print()
    print("COOKING INSTRUCTION")
    print()
    for cook in range(len(dire)-1):
        print(str(cook+1)+'.',dire[cook])

link=requests.get("https://www.allrecipes.com/").text
soup=BeautifulSoup(link,'html.parser')
data_container=soup.find_all(class_='recipeCard__imageLink',href=True,limit=15)

href=[item['href'] for item in data_container]

Recipi_id,ingrediant_section,cooking_instruction=[],[],[]

for url in href:
    linkk=requests.get(url).text
    soupp=BeautifulSoup(linkk,'html5lib')
    lst_ingredients_1=soupp.find(id="lst_ingredients_1")
    lst_ingredients_2=soupp.find(id="lst_ingredients_2")
    recipe_directions =soupp.find(class_="directions--section") 

    title=soupp.find('h1',class_="recipe-summary__h1") 
    if(title):
        Recipi_id.append(title.get_text())
        ing_text=lst_ingredients_1.find_all(class_="recipe-ingred_txt")
        ind=[]
        for i in ing_text_1:
            ind.append(i.get_text())

        ingrediant_section.append(ind)
        dire=[]
        direction=recipe_directions.find_all(class_="recipe-directions__list--item") 
        for i in direction:
            dire.append((i.get_text()).strip())
        cooking_instruction.append(dire)
        print_output(ind,dire)
    else: 
        title2=soupp.find('h1',class_="headline heading-content").get_text()
        Recipi_id.append(title2)
        ingrediant_container=soupp.find_all(class_="ingredients-item-name")
        ingrediant=[ (item.get_text()).strip() for item in ingrediant_container]
        direction_container=soupp.find_all(class_="paragraph")
        direct=[(item.find('p').get_text()).strip() for item in direction_container]
        Recipi_id.extend(title2)
        ingrediant_section.extend(ingrediant)
        cooking_instruction.extend(direct)
        print_output(ingrediant,direct)
