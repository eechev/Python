import requests

from pages.quotes_page import QuotesPage

PAGE_TO_SCRAPE = "http://quotes.toscrape.com"

page_content = requests.get(PAGE_TO_SCRAPE).content

quotes_page = QuotesPage(page_content)

quotes = quotes_page.quotes

for quote in quotes:
    print(f'Content: {quote.content}')
    print(f'Author {quote.author}')
    print(f'Tags: {", ".join(quote.tags)}')
    