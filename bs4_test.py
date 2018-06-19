import requests
from bs4 import BeautifulSoup
import os
import urllib
import urllib2
import csv
import json


page = requests.get("https://www.gamut.com/c/building-grounds")
soup = BeautifulSoup(page.text,'html.parser')

f = csv.writer(open('sample.csv', 'w'))
f.writerow(['Name','Link'])

x = soup.find(class_="categories__inner")

x = x.find_all('img')


for i in x:
    src = i.get('src')
    name = i.get('alt')
    f.writerow([name,src])
    print(src)
    print(name)


