import requests
from bs4 import BeautifulSoup
import csv
import random
from time import sleep

file = open('Gifts.csv', 'w', encoding='UTF-8_sig', newline='\n')
csv_obj = csv.writer(file)
csv_obj.writerow(['Description', 'Price', 'Symbol'])

pages = 1
url = f'https://www.etsy.com/search?q=gifts&ref=pagination&page={pages}'
lan = {'Accept-Language': 'en-US'}

while pages <= 5:
    resp = requests.get(url, headers=lan)
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')

    gifts = soup.find('ol', class_='wt-grid wt-grid--block wt-pl-xs-0 tab-reorder-container')
    soup_of_gifts = gifts.findAll('div', class_='v2-listing-card__info')
    # print(soup_of_gifts)

    for gift in soup_of_gifts:
        description = gift.h3.text
        price_obj = gift.select('.currency-value')
        for object in price_obj:
            price = object.text.strip()
            print(price)
        symbol_obj = gift.select('.currency-symbol')
        for object in symbol_obj:
            symbol = object.text.strip()


        csv_obj.writerow([description,price,symbol])
    pages += 1
    url = f'https://www.etsy.com/search?q=gifts&ref=pagination&page={pages}'
    sleep(random.randint(5, 10))

file.close()


