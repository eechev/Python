import logging
import re
from typing import List
from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocators
from parsers.books import BookParser

logger = logging.getLogger('scraping.books_page')

class BooksPage:
    def __init__(self, page) -> None:
        logger.info("Parsing page content with BeautifulSoup HTML parser")
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def books(self)  -> List[BookParser]:
        logger.info("getting books in page content")
        locator = BooksPageLocators.BOOKS
        books_tags = self.soup.select(locator)
        return [BookParser(e) for e in books_tags]
    
    @property
    def page_count(self) -> int:
        logger.info("getting total page count")
        page_locator = BooksPageLocators.PAGE
        page_count = self.soup.select(page_locator)[0].text
        matcher = re.search("Page [0-9]+ of ([0-9]+)", page_count)
        if matcher:
            return int(matcher.group(1))
        else:
            return 0