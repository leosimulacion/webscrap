from turtle import title
from bs4 import BeautifulSoup
import requests

# -*- coding: latin-1 -*-

web = 'https://www.elimparcial.com/sonora/sonora/Rinde-hoy-su-primer-informe-de-trabajo-Alfonso-Durazo-20221013-0002.html'
result = requests.get(web)
content = result.text.encode('latin-1')

soup = BeautifulSoup(content, 'lxml')

box = soup.find('div', class_='newsfull__title')

title = soup.find('h1').get_text()

transcript = soup.find('div', class_='newsfull__body').get_text()

#print(title)
#print(transcript)

with open('imparcial.txt', 'w') as file:
    file.write(title + transcript)
