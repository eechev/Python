from locators.quote_locators import QuoteLocators
from typing import List

class QuoteParser:
    """_summary_
    Given one of the specific quote divs, find out the data about
    the quote (quote content, author, tags).
    """
    
    def __init__(self, parent) -> None:
        self.parent = parent

    def __repr__(self) -> str:
        return f'<Quote {self.content}, by {self.author}>'
    
    @property
    def content(self) -> str:
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string
    
    @property
    def author(self) -> str:
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string
    
    @property
    def tags(self) -> List[str]:
        locator = QuoteLocators.TAG
        return [t.string for t in self.parent.select(locator)]