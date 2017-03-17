from __future__ import (absolute_import, print_function, division,
                        unicode_literals)


import re



from scrapy.loader.processors import Identity, Compose, MapCompose, Join



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

def get_ingredients(value):
    plus = int(len(value)/3)
    limit = int(len(value)*1/3)
    return value
def fix_ingredients(value):
    pass
class FamilyCircleLoader(SpiderLoader):
    name_out = Identity()
    img_url_out = Identity()
    direction_out = Compose(get_direction)
    servings_out = Compose(get_servings)
    products_out = Identity()
    ingredients_out = Compose(get_ingredients)
