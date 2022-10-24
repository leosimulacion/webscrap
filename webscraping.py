
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
from collections import Counter
import re

web = 'https://www.elimparcial.com/dinero/Riqueza-de-litio-en-Ucrania-Un-impulsor-para-la-invasion-rusa-20221023-0073.html '
result = requests.get(web)
content = result.text

soup = BeautifulSoup(content, 'lxml')

box = soup.find('div', class_='newsfull__title')

title = soup.find('h1').get_text()

transcript = soup.find('div', class_='newsfull__body').get_text()

with open('imparcial.txt', 'w') as file:
    file.write(title + transcript)

file_path='./imparcial.txt'

with open(file_path) as file:
    text = file.read()

#print(len(re.findall(r'\w+', text)))

counts = defaultdict(int)
for word in re.findall('\w+', text):
    counts[word] += 1

#print(counts)

counts =  Counter(re.findall('\w+', text))
print(counts)


counts =  Counter(re.findall('\w+', text))
#print(counts.most_common()[0])



