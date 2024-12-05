import logging
from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """_summary_
    Given one of the specific quote divs, find out the data about
    the quote (quote content, author, tags).
    """
    
    def __init__(self, parent) -> None:
        self.parent = parent

    def __repr__(self) -> str:
        
        return f'<Book {self.title}, Price {self.price}, Rating {self.rating}>'
    
    @property
    def title(self) -> str:
        logger.info("getting title")
        locator = BookLocators.TITLE
        item = self.parent.select_one(locator)
        return item.attrs['title']
    
    @property
    def price(self) -> str:
        logger.info('getting price')
        locator = BookLocators.PRICE
        item = self.parent.select_one(locator)
        #expression = '[0-9]*\\.[0-9]*'
        return item.text
    
    @property
    def rating(self) -> str:
        locator = BookLocators.RATING
        star_rating = self.parent.select_one(locator)
        classes = star_rating.attrs['class']
        return self._convert_to_num_string(list(filter(lambda x: x != 'star_rating', classes))[1])
    
    
    def _convert_to_num_string(self, value:str) -> str:
        value = value.lower()
        if value == 'one':
            return '1'
        elif value == "two":
            return "2"
        elif value == "three":
            return "3"
        elif value == "four":
            return "4"
        elif value == "five":
            return "5"
        else:
            return ""