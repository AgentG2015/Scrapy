# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS={
    'Host': 'www.cgwwo.com',
    'Connection': 'keep-alive',
    'Content-Length': '111',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.cgwwo.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.cgwwo.com/forum.php?mod=viewthread&tid=1681',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES={
    'Hm_lvt_2d57a0f88eed9744a82604dcfa102e49':r'1431695402',
    'Hm_lpvt_2d57a0f88eed9744a82604dcfa102e49':r'1432294524',
    'yXIa_2927_saltkey':r't1XD106R',
    'yXIa_2927_lastvisit':r'1432385205',
    '__jsluid':r'b73d26a9769b902f1fbe56a5e0876134',
    'yXIa_2927_ulastactivity':r'd0d1vw8AqyspEtpeh%2FHEGKdSfMnrN69p1IwF3bkuL17dfz9nypCD',
    'yXIa_2927_auth':r'37ecCvryoZtyEVvsoDjCnmyxXO59f03z9Lc93yQ1ULP4uO1PrHtdVB3EXlWgqUoajZwBCMjEp8F%2FsQB03lXJhwWERQ',
    'bdshare_firstime':r'1432389227439',
    'yXIa_2927_security_cookiereport':r'622dbrT3rqY0QNJNK43UU5HcFHsC0b0NRMKWB6028sU%2B6FAfS1LV',
    'yXIa_2927_connect_not_sync_t':r'1',
    'yXIa_2927_lip':r'123.157.77.150%2C1432404331',
    'yXIa_2927_nofavfid':r'1',
    'yXIa_2927_onlineusernum':r'141',
    'yXIa_2927_sendmail':r'1',
    'tjpctrl':r'1432410825378',
    'yXIa_2927_forum_lastvisit':r'D_82_1432396333D_92_1432401192D_76_1432409046',
    'yXIa_2927_visitedfid':r'76D92D36D44D40D104D60D38D61D75',
    'yXIa_2927_viewid':r'tid_1681',
    'yXIa_2927_sid':r'cS8LRA',
    'yXIa_2927_smile':r'2D1',
    'Hm_lvt_d49ab134993837af1ed6eb5dc65a4803':r'1432385631,1432387511,1432389104,1432394267',
    'Hm_lpvt_d49ab134993837af1ed6eb5dc65a4803':r'1432409041',
    'pgv_pvi':r'9919180015',
    'pgv_info':r'ssi=s4318814870',
    'yXIa_2927_lastact':r'1432409082%09forum.php%09post',
    'yXIa_2927_connect_is_bind':r'0'
}

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

url = r"http://www.cgwwo.com/forum.php?mod=post&action=reply&comment=yes&tid=1681&pid=3313&extra=&page=1&commentsubmit=yes&infloat=yes&inajax=1";
payload = {'formhash': '3f2dbaf6', 'handlekey': 'comment', 'message': u'看看                       看看'.encode("GBK"), 'commentsubmit': 'true'}

count = 0
while(True):
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES, timeout=10)
    except Exception as e:
        print e
        sys.stdout.flush()
        continue
    if u"帖子点评成功" in r.text:
        count += 1
        print "%s\t%i" % (filename, count)
        sys.stdout.flush()
    else:
        try:
            print r.text
        except:
            print "ascii error"
        sys.stdout.flush()
    time.sleep(31)
