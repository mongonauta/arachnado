# -*- coding: utf-8 -*-
"""
Default settings for Arachnado Scrapy spiders.
"""

DEPTH_STATS_VERBOSE = True
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
LOG_UNSERIALIZABLE_REQUESTS = True

# Turn it ON if the goal is to crawl the whole webiste
# (vs crawling most recent content):
PREFER_PAGINATION = False

# To enable autologin turn this option ON and pass AUTOLOGIN_URL
# (e.g. 'http://127.0.0.1:8089')
AUTOLOGIN_ENABLED = False
# AUTOLOGIN_URL = 'http://127.0.0.1:8089'

BOT_NAME = 'arachnado'
COOKIES_DEBUG = False
USER_AGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) '
              'AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/39.0.2148.0 Safari/537.36')

MB = 1024 * 1024
MEMUSAGE_ENABLED = True
DOWNLOAD_MAXSIZE = 1 * MB

# CLOSESPIDER_PAGECOUNT = 30  # for debugging
LOG_LEVEL = 'DEBUG'
TELNETCONSOLE_ENABLED = False
# CONCURRENT_REQUESTS = 100

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
CONCURRENT_REQUESTS_PER_DOMAIN = 4
DOWNLOAD_DELAY = 0.3  # min download delay

STATS_CLASS = 'arachnado.stats.EventedStatsCollector'
DOWNLOADER = 'arachnado.crawler_process.ArachnadoDownloader'

SPIDER_MIDDLEWARES = {
    'arachnado.spidermiddlewares.pageitems.PageItemsMiddleware': 100,
}

DOWNLOADER_MIDDLEWARES = {
    'arachnado.downloadermiddlewares.proxyfromsettings.ProxyFromSettingsMiddleware': 10,
    'autologin_middleware.AutologinMiddleware': 605,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'autologin_middleware.ExposeCookiesMiddleware': 700,
}

ITEM_PIPELINES = {
    'arachnado.pipelines.mongoexport.MongoExportPipeline': 10,
}

MONGO_EXPORT_ENABLED = True
MONGO_EXPORT_JOBID_KEY = '_job_id'
HTTPCACHE_ENABLED = False
# This storage is read-only. Responses are stored by PageExport middleware
HTTPCACHE_STORAGE = 'arachnado.pagecache.mongo.MongoCacheStorage'
