# -*- coding: utf-8 -*-

# Scrapy settings for movie_1905 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'movie_1905'

SPIDER_MODULES = ['movie_1905.spiders']
NEWSPIDER_MODULE = 'movie_1905.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movie_1905 (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 遵守robots协议
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求个数（越小越慢）
# CONCURRENT_REQUESTS = 10

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#下载延迟时间（越大请求越慢）
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'movie_1905.middlewares.Movie1905SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'movie_1905.middlewares.Movie1905DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'movie_1905.pipelines.Movie1905Pipeline': 1,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html

# 默认False;为True表示启用AUTOTHROTTLE扩展
#AUTOTHROTTLE_ENABLED = True

# The initial download delay

# 默认3秒;初始下载延迟时间
#AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies

# 默认60秒；在高延迟情况下最大的下载延迟
#AUTOTHROTTLE_MAX_DELAY = 10

# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

# 使用httpscatch缓存
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 1
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 缺省值: 0 一个整数值，指定最大的抓取响应(reponses)数。 如果spider抓取数超过指定的值，则会以 closespider_pagecount 的原因自动关闭。 
# 如果设置为0（或者未设置），spiders不会因为抓取的响应数而关闭。
#EXTENSIONS = {
#	'scrapy.extensions.closespider.CloseSpider': 500,
#}
# CLOSESPIDER_PAGECOUNT = 10

# 默认值: 0 一个整数值，单位为秒。如果一个spider在指定的秒数后仍在运行， 它将以 closespider_timeout 的原因被自动关闭。 
# 如果值设置为0（或者没有设置），spiders不会因为超时而关闭。
# CLOSESPIDER_TIMEOUT = 0