from __future__ import (absolute_import, print_function, division,

                                unicode_literals)

from pyscrapy.items import RecipeItem
from pyscrapy.loader.family_circle_loader import FamilyCircleLoader
from datetime import datetime
from scrapy.spiders import Rule

from six import text_type
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider
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
            Rule(
                 SgmlLinkExtractor(
                    allow=(
                        r'.+recipe/search/(\d+)'
                        )
                    )
                )

            )
    def parse_item(self,response):
        url=response.url
        print (response.url)
        loader = FamilyCircleLoader(
                item=RecipeItem(), response=response
                )
        crawl_time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        loader.add_value('crawl_time', text_type(crawl_time))
        loader.add_value('url', text_type(url))
        loader.add_xpath('name', '//h1[@class="title"]/text()') #remove /n on string
        loader.add_xpath('description', '//div[@class="nutritionfacts"]/text()') # join all text
        loader.add_xpath('img_url', '//img[@class="photo"]/@src')
        loader.add_xpath('servings','(//span[@class="yield"]/text())[1]') # remove servings word
        loader.add_xpath('prep_time','(//span[@class="min"]/text())[1]') # remove min word
        loader.add_xpath('direction', '//span[@class="direction-item-content"]/text()')
        loader.add_xpath('products', '//span[@class="name"]/text()') # rm all space in front, join
        loader.add_xpath('ingredients', '//span[@class="ingredientmeasure count"]/text()')
        loader.add_xpath('ingredients','//span[@class="amount"]/span[2]/text()')
        loader.add_xpath('ingredients', '//span[@class="name"]/text()') #add all per index
        yield loader.load_item()
