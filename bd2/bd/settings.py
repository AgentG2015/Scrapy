# -*- coding: utf-8 -*-

# Scrapy settings for bd project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bd'

SPIDER_MODULES = ['bd.spiders']
NEWSPIDER_MODULE = 'bd.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
RETRY_TIMES = 100
RETRY_HTTP_CODES = [400, 408]
RETRY_HTTP_CODES.extend(range(500,600))
CONCURRENT_REQUESTS = 10000
CONCURRENT_REQUESTS_PER_DOMAIN = 10000
LOG_LEVEL = 'WARNING'
