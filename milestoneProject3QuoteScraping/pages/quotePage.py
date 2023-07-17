from bs4 import BeautifulSoup

from milestoneProject3QuoteScraping.locators.pageQuoteLocator import PageLocator
from milestoneProject3QuoteScraping.parser.quotes import QuoteParser

class QuotePage:
    def __init__(self,page):
        self.soup=BeautifulSoup(page,'html.parser')

    @property
    def quotes(self):
        loc=PageLocator.QUOTE
        quotes_tags=self.soup.select(loc)
        return [QuoteParser(e) for e in quotes_tags]

