import scrapy
from scrapy.crawler import CrawlerProcess

from bd.spiders.sc import SCSpider

crawler_process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

crawler = crawler_process.create_crawler()
spider = crawler.spiders.create('sc')
crawler.crawl(spider)
crawler_process.start()