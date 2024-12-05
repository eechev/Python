import re
from typing import List
from bs4 import BeautifulSoup
from locators.books_page_locators import BooksPageLocators
from parsers.books import BookParser


class BooksPage:
    def __init__(self, page) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def books(self)  -> List[BookParser]:
        locator = BooksPageLocators.BOOKS
        books_tags = self.soup.select(locator)
        return [BookParser(e) for e in books_tags]
    
    @property
    def page_count(self) -> int:
        page_locator = BooksPageLocators.PAGE
        page_count = self.soup.select(page_locator)[0].text
        matcher = re.search("Page [0-9]+ of ([0-9]+)", page_count)
        if matcher:
            return int(matcher.group(1))
        else:
            return 0