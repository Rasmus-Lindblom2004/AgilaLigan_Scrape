import requests
from bs4 import BeautifulSoup

def get_sub_sites():
    all_links=[]
    for x in range(1,999):
        print(f'Start page {x}')
        r = requests.get(f'https://www.mathem.se/se/recipes/tags/4-vardag/?page={x}')
        if r.status_code == 500:
            break
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.find_all('a', class_="RecipeTile_card__LMqHF")

        for link in links:   
            all_links.append(link['href'])
    return all_links