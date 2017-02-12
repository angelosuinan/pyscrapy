# -*- coding: utf-8 -*-

# Scrapy settings for pyscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pyscrapy'

SPIDER_MODULES = ['pyscrapy.spiders']
NEWSPIDER_MODULE = 'pyscrapy.spiders'



# DOWNLOADER MIDDLEWARE SETTINGS
DOWNLOADER_MIDDLEWARES = {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            }
# GENERAL SETTINGS
BOT_NAME = 'pyscrapy'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
LOG_ENABLED = True
LOG_LEVEL = 'INFO'
LOG_FILE = None
FEED_FORMAT = 'csv'
FEED_URI = 'file:///tmp/spider-%(name)s-%(time)s.csv'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

# END GENERAL SETTINGS
# EXTENSION SETTINGS

EXTENSIONS = {
            'scrapy.extensions.logstats.LogStats': 500,
            'scrapy.extensions.corestats.CoreStats': 501,
            'scrapy.extensions.memusage.MemoryUsage': 502,
            'scrapy.extensions.closespider.CloseSpider': 503,
            'scrapy.extensions.throttle.AutoThrottle': 504,
            'pyscrapy.extensions.SpiderOpenCloseLogging': 505,
            }
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 256
STATS_DUMP = True
CLOSESPIDER_TIMEOUT = 60 * 60 * 8  # 8 hrs
CLOSESPIDER_ERRORCOUNT = 10000
EXTENSIONS_ENABLED = False
EXTENSIONS_CALLBACK = ''
EXTENSIONS_USER = ''
EXTENSIONS_PASS = ''

# END EXTENSION SETTINGS
# DOWNLOAD SETTINGS

AUTOTHROTTLE_ENABLED = True
CONCURRENT_ITEMS = 100
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 3
DOWNLOAD_DELAY = 5
DOWNLOAD_TIMEOUT = 60 * 5  # 5 mins
DOWNLOAD_MAXSIZE = 1024 * 1024 * 1024 * 2  # 2 gb
DOWNLOAD_WARNSIZE = 0  # Disabled
# END DOWNLOAD SETTINGS




# END DOWNLOADER MIDDLEWARE SETTINGS
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pyscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pyscrapy.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pyscrapy.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'pyscrapy.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
