import requests
from pages.book_page import BooksPage

SITE_TO_SCRAPE = 'https://books.toscrape.com'


page_content = requests.get(SITE_TO_SCRAPE).content

books_page = BooksPage(page_content)

books = books_page.books

# for book in books:
#     print(f'Title: {book.title}')
#     print(f"Price: {book.price}")
#     print(f'Rating: {book.rating} stars')






