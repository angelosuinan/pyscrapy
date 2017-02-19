
from datetime import datetime
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule

from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider

class familycircle(CrawlSpider):
    name = 'familycircle'
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
