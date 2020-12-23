# This is a simple api that sends an email everytime the price of
# the AOC 27 inch monitor drops below 250 dollars

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/AOC-C24G1-Frameless-DisplayPort-Adjustable/dp/B07GD5XG5G/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=10bo-20&linkId=d5ad17f91a3fbad6a79c7c579c00ccf1&language=en_US&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'htm.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[:-3])

    if(converted_price < 250):
        send_email()

    print(converted_price)
    print(title.strip())


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls
    server.ehlo()

    server.login('jrschmiedl8@gmail.com', 'password')

    subject = 'AOC 27" Price went down.'
    body = 'Check out the link https://www.amazon.com/AOC-C24G1-Frameless-DisplayPort-Adjustable/dp/B07GD5XG5G/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=10bo-20&linkId=d5ad17f91a3fbad6a79c7c579c00ccf1&language=en_US&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('jrschmiedl8@gmail.com', 'jr.schmiedl@yahoo.com', msg)

    print('Email has been sent.')

    server.quit()


# checks every day
while(True):
    check_price()
    time.sleep(60*60*24)