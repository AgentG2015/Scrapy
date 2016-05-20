import scrapy
from mrskin.items import *
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.xlib.pydispatch import dispatcher
from datetime import datetime

class MainSpider(CrawlSpider):
    name = "main"
    
    start_urls = [
        #url = 'http://www.mrskin.com/search/celebs?p=1'
    ]
    hostname = 'http://www.mrskin.com'
    start_urls.extend(["http://www.mrskin.com/search/celebs?p=%s" % page for page in xrange (1, 2)])
    items = []   
       
    def __init__(self):
        dispatcher.connect(self.finalize, scrapy.signals.engine_stopped)
        
    def finalize(self):
        print "done"
        
    def start_requests(self):
        count = len(self.start_urls)
        for i, url in enumerate(self.start_urls):
            print "%i/%i" % (i+1, count)
            request = Request(url, cookies = COOKIES, callback = self.parse_A)
            request.meta['url'] = url
            yield request
            
    def parse_A(self, response):
        nodes = response.xpath('//li[@class="span3"]')
        count = len(nodes)
        for i, node in enumerate(nodes):
            if i > 11110:
                break
            person = Person()
            person['id'] = i
            person['name'] = node.xpath('div[2]/a/text()').extract()[0]
            person['url'] = node.xpath('div[1]/a/@href').extract()[0]
            person['thumb'] = node.xpath('div[1]/a/img/@src').extract()[0]
            request = Request(self.hostname + person['url'], cookies = COOKIES, callback = self.parse_B)
            request.meta['person'] = person
            yield request
            
    def parse_B(self, response):
        nodes = response.xpath('//*[@id="movie-filmography"]//div[@class="drawer-item pic-gallery"]')
        person = response.meta['person']
        count = len(nodes)
        for i, node in enumerate(nodes):
            if i > 11110:
                break
                
            #initialization
            movie = Movie()  
            relation = PersonMovieRelation()            
            movie['id'] = i
            relation['id'] = i
            relation['pid'] = person['id']
            relation['mid'] = movie['id']
            
            #easy fields, no parse needed
            movie['name'] = node.xpath('div[1]/div[1]/div/a/text()').extract()[0]
            movie['url'] = node.xpath('div[1]/div[1]/div/a/@href').extract()[0]
            relation['nudity'] = node.xpath('div[1]/div[2]/div/span/text()').extract()[0].strip()
            parts_extract = node.xpath('div[1]/div[3]/div/button/@title').extract()
            relation['parts'] = "" if len(parts_extract) == 0 else parts_extract[0].strip()
            
            #raw string: " (2014) &ndash; as Everly", parse it to year and castAs
            div_str = node.xpath('div[1]/div[1]/div/text()').extract()[0].strip()          
            index = div_str.find(u'\u2013 as')
            movie['year'] = div_str[1:index-2]
            relation['castAs'] = div_str[index+5:]                                
            
            #video and image
            video_and_image_nodes = node.xpath('.//div[@class="thumbnail"]')
            videos = []
            images = []
            for resnode in video_and_image_nodes:
                #image node
                if len(resnode.xpath('a/span')) == 0:
                    #initialization
                    image = Image()
                    image['id'] = i
                    image['pid'] = person['id']
                    image['mid'] = movie['id']
                    
                    image['url'] = resnode.xpath('a/@href').extract()[0]
                    images.append(image)
                    
                #video node
                else:
                    #initialization
                    video = Video()
                    video['id'] = i
                    video['pid'] = person['id']
                    video['mid'] = movie['id']
                    
                    video['url'] = resnode.xpath('a/@href').extract()[0]
                    videos.append(video)
            
            print len(videos), "/", len(images), "/", len(video_and_image_nodes)
            
HEADERS = {
    'Host': 'www.mrskin.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    '__gads':r'ID=5a3dd499c49ba25e:T=1411190464:S=ALNI_Mac_CjbMaf273hC9lYFMYZUet6TnQ',
    'skticket':r'581ffd16e89ce4cfdc3389c257819a28_1547095255',
    'quality':r'hd',
    '__utma':r'14962480.679528866.1411190435.1413116882.1413154644.45',
    '__utmc':r'14962480',
    '__utma':r'169676413.1471585388.1411190435.1418866862.1418878442.146',
    '__utmc':r'169676413',
    '__utmz':r'169676413.1414597829.58.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'CNZZDATA1253762593':r'937432625-1420442645-http%253A%252F%252Fwww.mrskin.com%252F%7C1420442645',
    'SK_SESSID2':r'adaea205aad745a7b0f6898be47a82dc',
    'jwplayer.volume':r'0',
    'CNZZDATA1253762556':r'226860162-1420442897-http%253A%252F%252Fwww.mrskin.com%252F%7C1425605563',
    '_ga':r'GA1.2.1471585388.1411190435',
    '_gat':r'1',
    'auth2':r'NTNmZTMzOWRmZWFkNDIzNDRjOTAxMjNkNDY5YWJlM2Q1NTY2N2U3ZjoxNTQ3MDk1MjU1OiE%3D',
    '__mskb':r'~',
    '__mskc':r'~',
    '_cdata':r'[__mska=[v=311:s=~]:nomobile=~:plcn=1:aff_code=893181-1-2-57776]',
    'SK_SESSID2_AUTH_0c8cd':r'1432780415%3A574d72611680edf7139757dc102abb84%3A1%3A1435372415'
}