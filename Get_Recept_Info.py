import requests
from bs4 import BeautifulSoup

def get_recept_info(link):
    r=requests.get(f'https://www.mathem.se{link}')
    soup = BeautifulSoup(r.text, 'html.parser')

    img = soup.find_all('img', class_="k-image--cover")[12]['src']
    
    text = soup.find_all('span', class_="k-text-style--body-m")[24].get_text(separator='')
    
    ingredients_html = soup.find_all('table')
    ingredients_html = BeautifulSoup(f'<html><body>{ingredients_html[0]}</html></body>', "html.parser").find_all('tr')
    ingredients_list = []
    
    index = -1
    for ingredient in ingredients_html:
        ingredient = ingredient.text
        
        if ingredient[0].isalpha():
            index+=1
            ingredients_list.append([])

        ingredients_list[index].append(ingredient)

    instructions = soup.find_all('p')
    instructions_list = []

    for instruction in instructions[3:-1]:
        instruction=instruction.text

        if instruction == 'Bild: ':
            break

        instructions_list.append(instruction)
    print(instructions_list)
        



get_recept_info('/se/recipes/248-mari-bergman-gronsakspasta-med-artpesto-och-pumpakarnor/?portions=4')
# get_recept_info('/se/recipes/241-mari-bergman-fishn-chips-med-appelrora/?portions=4')
