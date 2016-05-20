import scrapy
from tutorial.items import *
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.utils.project import get_project_settings

class TorDown(CrawlSpider):
    name = "tordown"
    allowed_domains = ["tp.m-team.cc"]
    link_template = r"https://tp.m-team.cc/download.php?id="
    items = []
    start_urls = []
       
    def __init__(self):
        self.headers = HEADER
        self.cookies = COOKIES
        with open('items.txt', 'r') as f:
            self.items = f.read().split("\n")[0:-1]
        print len(self.items), "items"
        
    def start_requests(self):       
        for i, id in enumerate(self.items):
            #if i > 9: break
            url = self.link_template + id
            request = FormRequest(url,
                              headers = self.headers,
                              cookies =self.cookies,
                              callback = self.parse_item)
            request.meta['id'] = id
            yield request

    def parse_item(self, response):
        filename = "torrents/" + response.meta['id'] + ".torrent"
        with open(filename, 'wb') as f:
            f.write(response.body)
        
HEADER={
    "Host": "tp.m-team.cc",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36",
    "Referer": "https://tp.m-team.cc/torrents.php?sort=5&type=desc",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2"
}

COOKIES={
    'c_lang_folder':r'en',
    'c_secure_uid':r'MTU5NTI2',
    'c_secure_pass':r'd310dc816dd70e1425f042d8a6dc5b1c',
    'c_secure_ssl':r'eWVhaA%3D%3D',
    'c_secure_tracker_ssl':r'eWVhaA%3D%3D',
    'c_secure_login':r'bm9wZQ%3D%3D',
}          
    
            