from base import BaseList
from mutils import *

class CgmList(BaseList):
    name = "cgm"
    url_template = 'http://www.cgmodel.cn/home.php?mod=space&uid=%s&do=profile'
    start = 103500
    end = 874680   #874680           
    
    def parse_A(self, response):
        i = response.meta['i']
        username_raw = response.xpath('//*[@id="wp"]/div[4]/div/div[1]/h2/a/text()').extract()
        if len(username_raw) != 0:
            username = username_raw[0]
            last_active = response.xpath('//*[@id="pbbs"]/li[3]/text()').extract()[0].strip()
            if len(last_active) == 0:
                last_active = 'unknown' 
            gold_raw = response.xpath('//*[@id="psts"]/ul/li[4]/text()').extract()[0].strip()   
            gold = 0 if len(gold_raw) == 0 else int(gold_raw[:-1])
            if gold >= 100:
                self.populate([i, username, last_active, gold])
        else:
            p('%i not exist' % i)