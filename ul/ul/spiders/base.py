import scrapy
import os
import codecs
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.xlib.pydispatch import dispatcher
from mutils import *

class BaseList(CrawlSpider):
    name = "base"
    first = True
    step = 100
    url_template = ''
    start = 1
    end = 101
       
    def __init__(self):
        self.filename = self.name + ".txt"
        self.filename_tmp = self.name + "_tmp.txt"
        self.file_tmp = codecs.open(self.filename_tmp, 'a', 'utf-8')
        dispatcher.connect(self.finalize, scrapy.signals.engine_stopped)
        
    def finalize(self):
        self.file_tmp.close()
        
        #sort list
        list_tmp = []
        with codecs.open(self.filename_tmp, 'r', 'utf-8') as f:
            list = f.read().split('\n')
            for i in list:
                item = i.split('\t')
                list_tmp.append(item)  
        count = 0 if len(list_tmp) == 0 else len(list_tmp[0])
        list_tmp.sort(key = lambda x : int(x[count-1]), reverse = True)
        with codecs.open(self.filename, 'w', 'utf-8') as f: 
            first = True
            for item in list_tmp:
                if not first:
                    f.write('\n')
                else:
                    first = False
                count = len(item)
                for i, property in enumerate(item):
                    if i == count - 1:
                        f.write('%s' % property)
                    else:    
                        f.write('%s\t' % property)
        
        #final step
        os.remove(self.filename_tmp)
        p("done")
        
    def populate(self, item):
        if not self.first:
            self.file_tmp.write('\n')
        else:
            self.first = False
        count = len(item)
        for i, property in enumerate(item):
            if i == count - 1:
                self.file_tmp.write('%s' % property)
            else:
                self.file_tmp.write('%s\t' % property)
        self.file_tmp.flush()
        
    def start_requests(self):
        i = self.start
        while i < self.end:
            if (i) % self.step == 0:
                p("%i/%i" % (i, self.end))
            request = Request(self.url_template % i, callback = self.parse_A)
            request.meta['i'] = i
            i += 1
            yield request
            
    def parse_A(self, response):
        p(response.status)