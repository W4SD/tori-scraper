import requests
from time import sleep
from datetime import datetime
from bs4 import BeautifulSoup as BS
from format_date import get_datetime
import json

runtime = datetime.now()

URL = 'https://www.tori.fi/uusimaa/sisustus_ja_huonekalut/valaisimet?ca=18&cg=3020&c=3027&w=1&o=1'
response = requests.get(URL)

page = BS(response.text, "html.parser")

listings = page.find_all('a', class_='item_row_flex')

listing = listings[1]

product_listing = {}

for i,listing in enumerate(listings, start=1):
    print(i)
    # id element from listing as string (item_1234567)
    id = listing.get('id')
    # title of listing as string ('Kattovalaisin Kruunu')
    title = listing.find('div', class_="li-title").contents[0]
    # price of listing as string (42€), spaces removed
    price = listing.find('p', class_="list_price").contents[0].replace(" ", "") # '42€'
    # link to listing as URL (https://www.tori.fi/...)
    product_link = listing.get('href')
    # link to image of listing as URL (https://www.tori.fi/...)
    image_link = listing.find('div', class_="item_image_div").img['src']

    # scrape listing page and get the date listing was posted as custom date string (5 toukokuuta 23:02)
    listing_page = BS(requests.get(product_link).text, "html.parser")
    listing_page_date = listing_page.find('table', class_="tech_data").tr.find_all('td')[-1].get_text()

    # If listing is over 24h old, STOP!
    date = get_datetime(listing_page_date)
    is_over_24h = runtime - date
    if is_over_24h.days >= 1:
        break
    else:
        items = {
            "id": id,
            "title": title,
            "price": price,
            "product_link": product_link,
            "image_link": image_link,
            "time_stamp": date.strftime('%d.%m.%Y %H:%M')
        }
        product_listing[id] = items

    # print(f'Link: {product_link} type: {type(product_link)}')

print(json.dumps(product_listing))


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