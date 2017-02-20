# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class SpiderItem(Item):
    url = Field(serializers=unicode, required=True)
    crawl_time = Field(serializers=unicode, required=True)

class RecipeItem(SpiderItem):
    name = Field(serializers=unicode, required=True)
    price = Field(serializers=float, required=True)
    description = Field(serializers=unicode,)
    img_url = Field(serializers=unicode,)
    prep_time = Field(serializers=unicode,)
    servings = Field(serializers=unicode,)
    direction = Field(serializers=unicode,)
    products = Field(serializers=dict, )
    ingredients = Field(serializers=unicode,)

