import requests
from bs4 import BeautifulSoup as bs
import os

url = "https://www.pixiv.net/en/users/63601519/bookmarks/artworks"
html = requests.get(url)

soup = bs(html.content, "html.parser")

print(soup.prettify())

# tell what to search fo
box = soup.find(id="root")

#print()
#print(box)

#for element in imgs:
 ##   print(element)
