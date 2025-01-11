import requests
from bs4 import BeautifulSoup
import csv

#url = "https://cash.rbc.ru/cash/?currency=3&city=1&diapason=all"
#page = requests.get(url)
#soup = BeautifulSoup(page.text, "html.parser")

with open('Failed.html', 'rb') as f:
   soup = BeautifulSoup(f.read(), 'lxml')

offices = soup.find_all('div', class_='quote__office__one js-one-office')

with open('prices.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   field = ["name", "phone", "buy", "sell"]
   writer.writerow(field)
   for office in offices:
      phone = office.find_all('div', class_='quote__office__one__phone')[0].text
      name = office.find_all('a', class_='quote__office__one__name')[0].text
      buy = office.find_all('div', class_='quote__office__one__buy')[0].text
      buy = buy.replace("\n","")
      buy = buy.replace(" ","")
      buy = buy.replace("от","")
      sell = office.find_all('div', class_='quote__office__one__sell')[0].text
      sell = sell.replace("\n", "")
      sell = sell.replace(" ", "")
      sell = sell.replace("от", "")
      writer.writerow([name,phone,buy,sell])


