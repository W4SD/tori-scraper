import requests
from datetime import datetime
from bs4 import BeautifulSoup as BS
from format_date2 import get_datetime2
import json

runtime = datetime.now()
product_listing = {}
is_under24h = True
URL_page_no = 1

while is_under24h:

    URL = 'https://www.tori.fi/uusimaa/sisustus_ja_huonekalut/valaisimet?ca=18&cg=3020&c=3027&w=1&o=' + str(URL_page_no)
    print(URL)
    response = requests.get(URL)

    page = BS(response.text, "html.parser")
    listings = page.find_all('a', class_='item_row_flex')


    for i,listing in enumerate(listings, start=1):
        # print(i)
        # id element from listing as string (item_1234567)
        id = listing.get('id')
        # title of listing as string ('Kattovalaisin Kruunu')
        title = listing.find('div', class_="li-title").contents[0]
        # price of listing as string (42€), spaces removed, handle no price
        try:
            price = listing.find('p', class_="list_price").contents[0].replace(" ", "")
        except IndexError:
            price = "Ei ilmoitettu"
        # link to listing as URL (https://www.tori.fi/...)
        product_link = listing.get('href')
        # link to image of listing as URL (https://www.tori.fi/...)
        try:
            image_link = listing.find('div', class_="item_image_div").img['src']
        except AttributeError:
            image_link = "Ei kuvaa"

        listing_date = listing.find('div', class_="date_image").contents[0]

        # If listing is over 24h old, STOP!
        date = get_datetime2(listing_date)
        over_24h = runtime - date
        print(f'over_24h: {over_24h} --> is_over24h: {over_24h.days}')
        if over_24h.days >= 1:
            is_under24h = False
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

    URL_page_no = URL_page_no + 1
    print(f'page number: {URL_page_no} - listings:{len(product_listing)}')

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