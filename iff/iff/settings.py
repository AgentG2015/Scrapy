# -*- coding: utf-8 -*-

# Scrapy settings for iff project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iff'

SPIDER_MODULES = ['iff.spiders']
NEWSPIDER_MODULE = 'iff.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iff (+http://www.yourdomain.com)'
LOG_LEVEL = 'WARNING'
