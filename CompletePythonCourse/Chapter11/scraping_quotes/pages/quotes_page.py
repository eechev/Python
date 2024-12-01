from typing import List
from bs4 import BeautifulSoup
from locators.quote_page_locators import QuotesPageLocators
from parsers.quotes import QuoteParser

class QuotesPage:
    def __init__(self, page) -> None:
        self.soup = BeautifulSoup(page, 'html.parser')
    
    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotesPageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]