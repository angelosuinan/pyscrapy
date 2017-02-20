from __future__ import (absolute_import, print_function, division,

                                unicode_literals)

from pyscrapy.items import RecipeItem
from pyscrapy.loader.family_circle_loader import FamilyCircleLoader
from datetime import datetime
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider
class familycircle(CrawlSpider):
    name = 'family_circle'
    start_urls = [
                'http://www.familycircle.com/recipe/search/'
    ]
    rules = (
            Rule(
                SgmlLinkExtractor(
            allow=(
                r'..+recipe.+.',
                    ),
            restrict_xpaths=(
                r'//ul[@class="recipe-results"]',
                            ),
                ),
           callback='parse_item',
            ),

            )
    def parse_item(self,response):
        print (response.url)
        loader = FamilyCircleLoader(
                item=RecipeItem(), response=response
                )
