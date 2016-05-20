from base import BaseList
from mutils import *

class E3dList(BaseList):
    name = "e3d"
    url_template = 'http://www.element3ds.com/home.php?mod=space&uid=%s&do=profile'
    start = 1
    end = 33  #51640          
    
    def parse_A(self, response):
        i = response.meta['i']
        username_raw = response.xpath('//*[@id="wp"]/div[2]/div/div[1]/h2/a/text()').extract()
        if len(username_raw) != 0:
            username = username_raw[0]
            gold_raw = response.xpath('//*[@id="psts"]/ul/li[3]/text()').extract()[0].strip()            
            gold = 0 if len(gold_raw) == 0 else int(gold_raw)
            if gold >= 6000:
                self.populate([i, username, gold])
        else:
            p('%i not exist' % i)