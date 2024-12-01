import re
from bs4 import BeautifulSoup


ITEM_HTML = '''<html><head></head><body>
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
            <p class="price_color">£51.77</p>
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

soup = BeautifulSoup(ITEM_HTML, 'html.parser')

def find_item_name(soup):
    locator = 'article.product_pod h3 a' # finding through an hierarchy
    item_link = soup.select_one(locator)
    print(item_link.attrs['title'])
    print(item_link.attrs['href'])
    print(item_link.text)

def find_item_price(soup):
    locator = 'article.product_pod p.price_color'
    item_link = soup.select_one(locator)
    expression = '[0-9]*\\.[0-9]*'
    price = float(re.findall(expression, item_link.text)[0])
    print(price)
    # another way of doing the reg ex
    pattern = '£([0-9]+\\.[0-9]+)'
    matcher = re.search(pattern, item_link.text)
    if matcher:
        print(float(matcher.group(1)))
    else:
        print("Pattern not found")
    
def find_item_ratings(soup):
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']
    # rating_classes = [c for c in classes if c != 'star-rating']
    rating_classes = list(filter(lambda x: x != 'star-rating', classes))
    print(rating_classes[0])


find_item_name(soup)
find_item_price(soup)
find_item_ratings(soup)