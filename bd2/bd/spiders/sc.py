# -*- coding=UTF-8 -*-

import os
import sys
import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.xlib.pydispatch import dispatcher

class SCSpider(CrawlSpider):
    name = "sc"
    
    step = 100
    start = 476000
    end = 10 ** 7
    
    uk = '3544613589'
    # shareid = 747989750
    url_tpl = 'http://pan.baidu.com/share/init?shareid=%s&uk=' + uk
    
    res_folder = 'res/'
    list_200 = 'list_200.txt'
    list_302 = 'list_302.txt'
    list_others = 'list_others.txt'
       
    def __init__(self):
        dispatcher.connect(self.finalize, scrapy.signals.engine_stopped)
        if not os.path.exists(self.res_folder):
            os.makedirs(self.res_folder)
        self.file_200 = open(self.res_folder + self.list_200, 'w')
        self.file_302 = open(self.res_folder + self.list_302, 'w')
        self.file_others = open(self.res_folder + self.list_others, 'w')
        
    def finalize(self):
        self.file_200.close()
        self.file_302.close()
        self.file_others.close()
        print "done"
        
    def pad(self, number):
        return (4 - len(number)) * '0' + number
        
    def start_requests(self):
        for i in xrange(self.start, self.end):
            if i % self.step == 0:
                print 'momo: %i/%i' % (i, self.end)
                sys.stdout.flush()
            shareid = i
            url = self.url_tpl % shareid
            request = Request(url, method='HEAD', callback=self.parse_A, dont_filter=True)
            request.meta['dont_redirect'] = True
            request.meta['handle_httpstatus_list'] = [302]
            yield request
        
    def parse_A(self, response):
        if response.status == 302:
            if response.headers['Location'] != 'http://pan.baidu.com/error/404.html':
                self.file_302.write(response.headers['Location'])
                self.file_302.flush()
        elif response.status == 200:
            self.file_200.write(response.url)
            self.file_200.flush()
        else:
            self.file_others.write(response.status + '\t' + response.url)
            self.file_others.flush()
            
    def parse_B(self, response):
        res = response.xpath('//*[@id="share_nofound_des"]/text()').extract()[0].strip()
        comp = u'啊哦，你来晚了，分享的文件已经被取消了，下次要早点哟。'
        print (res == comp)
            
HEADERS = {
    'Host': 'pan.baidu.com',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Origin': 'http://pan.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}