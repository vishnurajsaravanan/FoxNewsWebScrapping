import requests
from bs4 import BeautifulSoup

URL = "https://www.foxnews.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
headline_elems = soup.find_all("h2", class_="title")

for headline_elem in headline_elems:
    link_elem = headline_elem.find("a")
    if link_elem is not None:
        print(link_elem.text.strip())
        print(link_elem["href"])
        print()
