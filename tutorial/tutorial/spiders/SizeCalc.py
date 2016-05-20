import scrapy
from tutorial.items import *
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request,FormRequest
from scrapy.utils.project import get_project_settings

class SizeCalc(CrawlSpider):
    name = "sizecalc"
    allowed_domains = ["tp.m-team.cc"]
    start_urls = [
        #"https://tp.m-team.cc/adult.php?inclbookmarked=0&incldead=1&spstate=0&&sort=5&type=asc&page=%s" % page for page in xrange (0, 1)     
    ]
    start_urls.extend(["https://tp.m-team.cc/torrents.php?inclbookmarked=0&incldead=1&spstate=0&&sort=5&type=asc&page=%s" % page for page in xrange (0, 36)])   
    
    total_items = 0
    total_size = 0.0 
       
    def __init__(self):
        self.file = open('items.txt', 'wb')
        self.headers = HEADER
        self.cookies = COOKIES
        
    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url,
                              headers = self.headers,
                              cookies =self.cookies,
                              callback = self.parse_item)                            

    def parse_item(self, response):
        nodes = response.xpath('//*[@id="form_torrent"]/table/tr[not(@class)]')
        subTotal = 0.0
        i = 0
        for i, node in enumerate(nodes):
            if i == 0:
                continue
            item = MTItem()
            item['id'] = node.xpath('.//td[@class="embedded"][1]/a/@href').re(r'id=(\d+)')[0]
            item['title'] = node.xpath('.//td[@class="embedded"][1]/a/b/text()').extract()[0]
            temp = node.xpath('td[5]/text()').extract()
            item['size'] = float(temp[0])
            item['unit'] = temp[1]
            stateColor = node.xpath('td[9]/@style').extract()[0]
            stateText = node.xpath('td[9]/text()').extract()[0]
            if stateText == '--':
                item['state'] = 0
            elif 'blue' not in stateColor:
                item['state'] = 1
            else:
                item['state'] = 2
            tempSize = 0.0
            if item['unit'] == 'KB':
                tempSize = item['size']
            elif item['unit'] == 'MB':
                tempSize = item['size'] * 1024
            elif item['unit'] == 'GB':
                tempSize = item['size'] * 1048576
            subTotal += tempSize
            self.file.write(item['id']+"\n")
        
        self.total_size += subTotal
        self.total_items += i
        print i, "items"
        print_readable_format(subTotal)
        print self.total_items, "items"
        print_readable_format(self.total_size)
        print '----------------------------'

def print_readable_format(size):
        if size < 1024:
            print('%.2f%s' % (size, 'KB'))
        elif size > 1024 and size < 1048576:
            print('%.2f%s' % (size/1024, 'MB'))
        else:
            print('%.2f%s' % (size/1048576, 'GB'))
        
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
    
            