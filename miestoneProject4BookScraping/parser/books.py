from miestoneProject4BookScraping.locators.bookLocator import BookLocator
import re

class BookParser:

    def __init__(self,parent):
        self.parent=parent

    def __repr__(self):
        return f'Book {self.title}, Has {self.rating} star rating and is of {self.price}'

    rating_number={'One':1,'Two':2,'Three':3,"Four":4,'Five':5}

    @property
    def title(self):
        loc=BookLocator.TITLE
        return self.parent.select_one(loc).attrs['title']

    @property
    def rating(self):
        loc=BookLocator.RATING
        r=self.parent.select_one(loc).attrs['class']
        rat=[i for i in r if i!='star-rating']
        ratings=BookParser.rating_number[rat[0]]
        return ratings

    @property
    def price(self):
        loc=BookLocator.PRICE
        p=self.parent.select_one(loc).string
        pattern='£([0-9]+\.[0-9]+)'
        price=re.search(pattern,p)
        return float(price.group(1))


