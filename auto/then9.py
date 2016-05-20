# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS={
    'Host': 'www.then9.com',
    'Connection': 'keep-alive',
    'Content-Length': '75',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.then9.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.then9.com/forum.php?mod=viewthread&tid=18616&extra=pageD1%3D&page=13',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES={
    'YpM5_2132_saltkey':r'wq4999Sq',
    'YpM5_2132_lastvisit':r'1432143236',
    'YpM5_2132_ulastactivity':r'f8fcyzDA%2Fw8q7tnipoS9T9IxJ7kosF81oA1hQ2hMah4Sw4zibSj%2F',
    'YpM5_2132_auth':r'be7cMM8%2FhN%2FCYzg6O5FpcZKuKjuSkFOPWrdYEGw13BfY9pjAIlKOFJmul3k0bA8F5tZ%2FSZsdKVfM6Bu2G9HA2pdi9Bg',
    'YpM5_2132_security_cookiereport':r'5cd42ofHLAsmI3rYABN6GGXG4f94oQqBsIoKGDLNj2TWK46qfl4L',
    'YpM5_2132_secqaa':r'1316.50fb0888ac66370dcd',
    'YpM5_2132_nofavfid':r'1',
    'tjpctrl':r'1432317992826',
    'YpM5_2132_home_diymode':r'1',
    'YpM5_2132_connect_last_sync_t':r'1',
    'YpM5_2132_visitedfid':r'47D71D60D38D83D77D76D40',
    'YpM5_2132_sendmail':r'1',
    'YpM5_2132_st_t':r'286422%7C1432316613%7C096b9f7341d8fe9a35103602ecb450be',
    'YpM5_2132_forum_lastvisit':r'D_47_1432316613',
    'YpM5_2132_connect_not_sync_t':r'1',
    'YpM5_2132_viewid':r'tid_18616',
    'YpM5_2132_sid':r'TPXp81',
    'pgv_pvi':r'5051629640',
    'pgv_info':r'ssi=s562760440',
    'YpM5_2132_checkpm':r'1',
    'Hm_lvt_85a6375b3e84bfea76cd625df784b04e':r'1432312682,1432313328,1432314390,1432315957',
    'Hm_lpvt_85a6375b3e84bfea76cd625df784b04e':r'1432316680',
    'CNZZDATA5678147':r'cnzz_eid%3D29072671-1432144218-null%26ntime%3D1432311383',
    'YpM5_2132_st_p':r'286422%7C1432316707%7Ca7e953b71bb4a06527248a939acb73ac',
    'YpM5_2132_smile':r'1D1',
    'YpM5_2132_lastact':r'1432316714%09forum.php%09ajax',
    'YpM5_2132_connect_is_bind':r'0'
}

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

url = r"http://www.then9.com/forum.php?mod=post&action=reply&comment=yes&tid=18616&pid=223439&extra=pageD1%3D&page=13&commentsubmit=yes&infloat=yes&inajax=1";
payload = {'formhash': '63552b25', 'handlekey': 'comment', 'message': u'看看'.encode("GBK"), 'commentsubmit': 'true'}

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
    time.sleep(1500)
