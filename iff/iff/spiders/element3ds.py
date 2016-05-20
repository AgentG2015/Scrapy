import scrapy
from iff.items import PListItem
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.xlib.pydispatch import dispatcher

class Element3dsSpider(CrawlSpider):
    name = "e3d"
    allowed_domains = ["www.element3ds.com"]
    start_urls = [
        http://www.element3ds.com/plugin.php?id=it618_tietuibang:tui&uid=12572&tid=30254  
    ] 
       
    def __init__(self):
        self.httpHash = {}
        self.socks5Hash = {}
        self.httpFile = open('http.txt', 'w')   
        self.socks5File = open('socks5.txt', 'w')  
        dispatcher.connect(self.finalize, scrapy.signals.engine_stopped)
        
    def finalize(self):
        for item in sorted(self.httpHash.itervalues(), key=lambda i: int(i["response"])):
            self.httpFile.write("%s\t%s\t%s\t%s\t%s\n" % (item["ip"], item["port"], item["protocol"], item["anonymity"], item["response"]))
        self.httpFile.close()
        for item in sorted(self.socks5Hash.itervalues(), key=lambda i: int(i["response"])):
            self.socks5File.write("%s\t%s\t%s\t%s\t%s\n" % (item["ip"], item["port"], item["protocol"], item["anonymity"], item["response"]))
        self.socks5File.close()
        
    def start_requests(self):
        count = len(self.start_urls)
        for i, url in enumerate(self.start_urls):
            print "%i/%i" % (i+1, count)
            yield Request(url,
                          headers = HEADERS,
                          callback = self.parse_item)                            

    def parse_item(self, response):
        print response.status
        
HEADERS={
    'Host': 'free-proxy.cz',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}          
    
            