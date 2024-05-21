import requests
from bs4 import BeautifulSoup

def get_recept_info(link):
    r=requests.get(f'https://www.mathem.se{link}')
    soup = BeautifulSoup(r.text, 'html.parser')
    
    title = get_title(soup)
    img = get_image(soup)
    description = get_description(soup)
    ingredients = get_ingrediens(soup)
    instructions = get_instructions(soup)
    time = get_time(soup)

    return (title, img, description, ingredients, instructions, time)

def get_title(soup):
    return soup.h1.text

def get_image(soup):
    return soup.find_all('img', class_="k-image--cover")[12]['src']

def get_description(soup):
    description = soup.find_all('span', class_="k-text-style--body-m")[24].text.split('\n')
    return description[0]

def get_ingrediens(soup):
    ingredients_html = soup.find_all('table')
    ingredients_html = BeautifulSoup(f'<html><body>{ingredients_html[0]}</html></body>', "html.parser").find_all('tr')
    ingredients_list = []

    index = -1
    for ingredient in ingredients_html:
        ingredient = ingredient.text.strip()

        if ingredient=='':
            index+=1
            ingredients_list.append([])
            ingredients_list[index].append('Ingredienser')

        elif ingredient[0].isalpha():
            index+=1
            ingredients_list.append([])
            ingredients_list[index].append(ingredient)

        else:
            ing = ""
            flag=False
            for letter in ingredient:
                if not letter.isupper() or flag:
                    ing += letter
                elif not flag:
                    flag = True
                    ing += f' {letter}'
            ingredients_list[index].append(ing)
   
    return tuple(ingredients_list)

def get_instructions(soup):
    instructions = soup.find_all('p', class_=None)
    instructions_list = []

    for instruction in instructions:
        instruction=instruction.text

        if instruction[0:13] == 'Näringsvärde:' or instruction == 'Bild: ' or instruction[0:8] == 'Styling:':
            break

        instructions_list.append(instruction)

    return tuple(instructions_list)

def get_time(soup):
    return soup.find_all('span', class_='k-text-style--label-xs')[30].text

get_recept_info('/se/recipes/3582-mari-bergman-omelett-med-ost-och-kalkon/')