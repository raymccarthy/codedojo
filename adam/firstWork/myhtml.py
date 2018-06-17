import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
response = urllib.request.urlopen('https://www.vocabulary.com/lists/52473', context=context)

soup = BeautifulSoup(response, "html.parser")

for a in soup.find_all('a','word dynamictext'):
    print(a.string)

# print(html)

# soup = bs4.BeautifulSoup(pg.split("<h1>",1)[-1])
# print(soup.find_all("p")[:3])
# soup = bs4.BeautifulSoup4(htmlf)
# res2 = subsoup.find('h1',attrs={'itemprop':'name'})
# if res2:
#     print(res2.get_text())

