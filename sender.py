import os, scraper
import time
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup

url = 'https://www.blockchain.com/ru/explorer'
response = requests.get(url)
html_page = BeautifulSoup(response.text, "lxml")
btc_price = html_page.find('span', class_='sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC sc-1mty1jv-2 dXBjzl')



account_sid = 'AC65d005388370dad0a3916e5720330bb5'
auth_token = '36a63e09d159c0753920d484942d2fb7'
client = Client(account_sid, auth_token)

while True:
    message = client.messages \
        .create(
             body=btc_price.text,
             from_='+19255237003',
             to='+380665954053'
         )

    time.sleep(3600)

print(btc_price)