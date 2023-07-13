import re
from bs4 import BeautifulSoup

middle_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">$51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''
class Parsing:
    def __init__(self,page):
        self.soup= BeautifulSoup(page,'html.parser')

    def find_item_name(self):
        loc='article.product_pod h3 a'   #using the relative postion of the info
        item_link= self.soup.select_one(loc)
        item_name= item_link.attrs['title']
        return item_name

    def find_link(self):
        loc='article.product_pod h3 a'
        item_link= self.soup.select_one(loc)
        item=item_link.attrs['href']
        return item

    def find_price(self):
        loc = 'article.product_pod p.price_color'
        itemprice =  self.soup.select_one(loc).string
        pattern = '\$([0-9]+\.[0-9]+)'
        match = re.search(pattern, itemprice)
        return float(match.group(1))

    def find_rating(self):
        loc = 'article.product_pod p.star-rating'
        rating_tag = self.soup.select_one(loc)
        classes = rating_tag.attrs['class']
        rating_class = [i for i in classes if i != 'star-rating']
        return rating_class[0]

item = Parsing(middle_HTML)
print(item.find_item_name())
