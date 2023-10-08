import requests
import os
import dotenv
import lxml
from bs4 import BeautifulSoup
import smtplib

dotenv.load_dotenv()

YOUR_SMTP_ADDRESS = os.getenv("YOUR_SMTP_ADDRESS")
YOUR_EMAIL = os.getenv("YOUR_EMAIL")
YOUR_PASSWORD = os.getenv("YOUR_PASSWORD")
User_Agent = os.getenv("User-Agent")


URL = "https://www.amazon.in/dp/B0BDJ6ZMCC"     # Enter the link here
BUY_PRICE = 120000                              # Enter the buy price here


header = {
    "User-Agent": User_Agent,
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)

print(response)

soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())

price = soup.find(class_="a-price-whole").get_text()
title = soup.find(id="productTitle").get_text().strip()

price_concat = ""
for i in price.split(","):
    price_concat += i

price_float = float(price_concat)
print(price_float)


if price_float <= BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
