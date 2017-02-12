import logging
from scrapy import signals
from scrapy.exceptions import NotConfigured

logger = logging.getLogger(__name__)

class SpiderOpenCloseLogging(object):
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        if (
            not crawler.settings.getbool('EXTENSIONS_ENABLED') and
            not crawler.settings.get('EXTENSIONS_CALLBACK') and
            not crawler.settings.get('EXTENSIONS_USER') and
            not crawler.settings.get('EXTENSIONS_PASS')
        ):
            raise NotConfigured
        ext = cls()
        crawler.signals.connect(ext.spider_opened,
                                signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed,
                                signal=signals.spider_closed)
        return ext
    def spider_opened(self, spider):
        logger.info("opened spider %s", spider.name)
    def spider_closed(self, spider):
        if not hasattr(spider, 'spider_params'):
            raise NotConfigured
        timefmt = '{:%Y-%m-%dT%H:%M:%SZ}'
        feedtimefmt = '{:%Y-%m-%dT%H-%M-%S}'
        stats = spider.crawler.stats.get_stats()
        stats['start_time'] = timefmt.format(stats['start_time'])
        stats['finish_time'] = timefmt.format(stats['finish_time'])
        updates = {
            'item_scraped_count': stats.get('item_scraped_count'),
            'job_start_time': stats.get('start_time'),
            'job_finish_time': stats.get('finish_time'),
            'finish_reason': stats.get('finish_reason'),
           # 'stats': json.dumps(stats),
          #  'archive_file': feed_uri,
            'log_file': spider.settings.get('LOG_FILE'),
            'status': self.FINISHED,
        }
        for k, v in updates.items():
            logger.info('Updated {} to {}'.format(k, v))
