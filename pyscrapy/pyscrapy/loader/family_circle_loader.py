from __future__ import (absolute_import, print_function, division,
                        unicode_literals)


import re



from scrapy.loader.processors import Identity, Compose, MapCompose



from bs4 import BeautifulSoup
from .base import SpiderLoader


from six import text_type

def get_direction(value):
    for x in value:
        value[value.index(x)] = str(value.index(x)+1) +"  "+ x
    return (value)

def get_servings(value):
    value[0]=' '.join(value[0].split())
    return value

def get_products(value):
    print (value)

def get_ingredients(value):
    print (value)
class FamilyCircleLoader(SpiderLoader):
    name_out = Identity()
    img_url_out = Identity()
    direction_out = Compose(get_direction)
    servings_out = Compose(get_servings)
    products_out = Compose(get_products)
    ingredients_in = Compose(get_ingredients)
