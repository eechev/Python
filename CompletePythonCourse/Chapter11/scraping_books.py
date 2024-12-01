import requests
from bs4 import BeautifulSoup

WEB_SITE_TO_SCRAPE = "https://books.toscrape.com/"

page = requests.get(WEB_SITE_TO_SCRAPE)
soup = BeautifulSoup(page.content, "html.parser")
h1_tags = soup.find_all("h1")

for h1_tag in h1_tags:
    print(h1_tag.text)