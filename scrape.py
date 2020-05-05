import requests
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup as BS


URL = 'https://www.tori.fi/uusimaa/sisustus_ja_huonekalut/valaisimet?ca=18&cg=3020&c=3027&w=1&o=1'
response = requests.get(URL)

page = BS(response.text, "html.parser")

listings = page.find_all('a', class_='item_row_flex')

listing = listings[1]

id = listing.get('id') # 'item_1234567'
title = listing.find('div', class_="li-title").contents[0] # 'Kattovalaisin Kruunu'
price = listing.find('p', class_="list_price").contents[0].replace(" ", "") # '42€'
product_link = listing.get('href') # https://www.tori.fi/...
image_link = listing.find('div', class_="item_image_div").img['src'] # https://www.tori.fi/...


print(f'Image src: {image_link} type: {type(image_link)}')
print(f'Link: {product_link} type: {type(product_link)}')

# print(len(listings), listings[1])




print(f'current time:{datetime.now()}')


# Hakuja niin kauan että viime hauysta 24h .. / time now - 24h
# tulokset listaan.. -> Kuvat, otsikot , linkit, hinta.. --> Kuva ja 3 riviä.. dessu?
# lista jsonmuotoon tahi vastaava .. heroku deployment? flask ?
# telegram botti käy noukkimassa llistan / botti kutsu / autocall listaan
# printtaa 24h listat ryhmään

# optioita:
# tuotteet jota seuraataan
# alueet jota seurataan
# aikaväli noudoille

#bottiin:
# - linkeille "x" täppä jota voi painaa ja tulos poistuu .. -> vaatii esim 2x"x"



# https://medium.com/better-programming/how-to-scrape-multiple-pages-of-a-website-using-a-python-web-scraper-4e2c641cff8
# https://realpython.com/beautiful-soup-web-scraper-python/

# heroku deployment with cron
# https://saqibameen.com/deploy-python-cron-job-scripts-on-heroku/