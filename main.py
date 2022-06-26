from bs4 import BeautifulSoup
import requests
import re

html_test = requests.get(
    'https://store.playstation.com/en-hk/pages/browse').text

soup = BeautifulSoup(html_test, 'lxml')
game_list = soup.find_all(
    'li', class_='psw-l-w-1/2@mobile-s psw-l-w-1/2@mobile-l psw-l-w-1/6@tablet-l psw-l-w-1/4@tablet-s psw-l-w-1/6@laptop psw-l-w-1/8@desktop psw-l-w-1/8@max')
for game in game_list:
    gameTitle = game.find(
        'span', class_='psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2').text
    href = game.div.a['href']
    print(f'''
    Game title: {gameTitle}
    URL: https://store.playstation.com/{href}
    ''')
    detail = requests.get('https://store.playstation.com/' + href).text
    soup_detail = BeautifulSoup(detail, 'lxml')
    price_box = soup_detail.find(
        'div', class_='psw-c-bg-card-1 psw-p-y-7 psw-p-x-8 psw-m-sub-x-8 psw-m-sub-x-6@below-tablet-s psw-p-x-6@below-tablet-s')
    price = price_box.find('span', class_='psw-t-title-m').text
    with open('data/psList.csv', 'a') as f:
        f.write(f"{gameTitle},{price} \n")
