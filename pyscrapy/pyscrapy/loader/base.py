from scrapy.contrib.loader import ItemLoader

from scrapy.contrib.loader.processor import Join, MapCompose



from six import text_type





class SpiderLoader(ItemLoader):

    default_input_processor = MapCompose(text_type.strip)

    default_output_processor = Join()

    #sample
    """

    url_in =
    url_out =

    """
