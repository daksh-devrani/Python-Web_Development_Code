import requests
from miestoneProject4BookScraping.pages.booksPage import BookPage

content=requests.get('http://books.toscrape.com').content
page=BookPage(content)
books=page.book

