import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/dp/B0BDJ6ZMCC"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)

print(response)
# print(response.text)

soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()

print(price)
# price_without_comma = price.split(",")
# print(price_without_comma)
# print(price_without_comma[0], price_without_comma[1])
