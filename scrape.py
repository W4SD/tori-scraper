import requests


URL = 'https://www.tori.fi/uusimaa/sisustus_ja_huonekalut/valaisimet'
page = requests.get(URL)

print(page)