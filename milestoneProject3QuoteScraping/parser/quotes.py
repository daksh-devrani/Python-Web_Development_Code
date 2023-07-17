from milestoneProject3QuoteScraping.locators.quoteLocator import QuoteLocator

class QuoteParser:
    '''given one of the specific div tags, find out about the content'''

    def __init__(self,parent):
        self.parent=parent

    def __repr__(self):
        return f'Quote {self.content}, by {self.author}, with {self.tags} tags'

    @property
    def content(self):
        loc=QuoteLocator.CONTENT
        return self.parent.select_one(loc).string

    @property
    def author(self):
        loc=QuoteLocator.AUTHOR
        return self.parent.select_one(loc).string

    @property
    def tags(self):
        loc=QuoteLocator.TAGS
        return [e.string for e in self.parent.select(loc)]
