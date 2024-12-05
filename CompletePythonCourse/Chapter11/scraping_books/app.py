import logging
import requests
from pages.book_page import BooksPage

logging.basicConfig(
    format='%(asctime)s - %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
    level=logging.INFO,
    filename='./CompletePythonCourse/Chapter11/scraping_books/app.log')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get("https://books.toscrape.com").content
books_page = BooksPage(page_content)
books = books_page.books
page_count = books_page.page_count


for p in range(1, page_count):
    page_to_scrape = f'https://books.toscrape.com/catalogue/page-{p + 1}.html'
    page_content = requests.get(page_to_scrape).content
    books_page = BooksPage(page_content)
    books.extend(books_page.books)

# for book in books:
#     print(f'Title: {book.title}')
#     print(f"Price: {book.price}")
#     print(f'Rating: {book.rating} stars')






