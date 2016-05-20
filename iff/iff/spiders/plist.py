import scrapy
from iff.items import PListItem
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.xlib.pydispatch import dispatcher

class PListSpider(CrawlSpider):
    name = "plist"
    allowed_domains = ["free-proxy.cz"]
    start_urls = [
        #http://free-proxy.cz/en/proxylist/country/all/all/speed/all/1  
    ]
    start_urls.extend(["http://free-proxy.cz/en/proxylist/country/all/all/speed/all/%s" % page for page in xrange (1, 251)])   
       
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
        if response.status != 200:
            print "-----------------------------------------------------------"
            print "Not 200: %s" % response.url
            print "-----------------------------------------------------------"
        nodes = response.xpath('//*[@id="proxy_list"]/tbody/tr')
        for node in enumerate(nodes):
            item = PListItem()
            item["ip"] =  node[1].xpath('td[1]/text()').extract()[0][1:]
            if len(item["ip"]) > 0:
                item["port"] = node[1].xpath('td[2]/span/text()').extract()[0]
                item["protocol"] = node[1].xpath('td[3]/small/text()').extract()[0]
                item["anonymity"] = node[1].xpath('td[7]/small/text()').extract()[0]
                item["response"] = node[1].xpath('td[10]/div/small/text()').extract()[0][:-3]
                if item["protocol"] == "HTTP":
                    self.httpHash[item["ip"]] = item
                if item["protocol"] == "SOCKS5":
                    self.socks5Hash[item["ip"]] = item
        
HEADERS={
    'Host': 'free-proxy.cz',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}          
    
            