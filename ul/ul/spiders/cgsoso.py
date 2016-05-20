from base import BaseList
from mutils import *

class CgsosoList(BaseList):
    name = "cgsoso"
    url_template = 'http://www.cgsoso.com/?%s'
    start = 1
    end = 51   #52061     
    
    def parse_A(self, response):
        i = response.meta['i']
        username_raw = response.xpath('//*[@id="profile_content"]/div/div/h2/a/text()').extract()
        if len(username_raw) != 0:
            username = username_raw[0]
            gold_raw = response.xpath('//*[@id="statistic_content"]/div/ul/li[5]/a/text()').extract()[0]
            gold = 0 if gold_raw == '--' else int(gold_raw)
            if gold >= 20:
                self.populate([i, username, gold])
        else:
            p('%i not exist' % i)