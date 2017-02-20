from __future__ import (absolute_import, print_function, division,
                        unicode_literals)


import re



from scrapy.contrib.loader.processor import Identity, Compose, MapCompose



from bs4 import BeautifulSoup
from .base import SpiderLoader


from six import text_type


class FamilyCircleLoader(SpiderLoader):
    img_url_out = Identity()
