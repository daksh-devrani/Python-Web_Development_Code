from bs4 import BeautifulSoup

from miestoneProject4BookScraping.locators.pageBookLocator import PageLocator
from miestoneProject4BookScraping.parser.books import BookParser

class BookPage:
    def __init__(self,page):
        self.soup=BeautifulSoup(page, 'html.parser')

    @property
    def book(self):
        loc=PageLocator.BOOKS
        par=self.soup.select(loc)
        return [BookParser(e) for e in par]


