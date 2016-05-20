# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS = {
    'Host': 'www.element3ds.com',
    'Connection': 'keep-alive',
    'Content-Length': '69',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.element3ds.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 115Browser/5.1.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.element3ds.com/forum.php?mod=viewthread&tid=35089&extra=&page=11',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8'
}

COOKIES = {
    'tjpctrl':r'1433652474621',
    '9ZW4_2132_saltkey':r'G4WPug6g',
    '9ZW4_2132_lastvisit':r'1433647110',
    '9ZW4_2132_ulastactivity':r'c77evTnTLFblbKa4%2FF%2BUnhdjThertrLIeMMKWLCa6WN16z%2F7Bp9N',
    '9ZW4_2132_auth':r'f0c4kIYs2ULTW3Cw1GeE4SvMyAJI3jJu1a7jpzADDq13xIzBy9Ljo%2FNfTKaGuIdINxj7nfTMTBcpdUm0DU93NDnhsg',
    '9ZW4_2132_home_diymode':r'1',
    '9ZW4_2132_taskdoing_52909':r'1',
    '9ZW4_2132_nofavfid':r'1',
    '9ZW4_2132_onlineusernum':r'953',
    '9ZW4_2132_st_t':r'52909%7C1433650915%7C5eee1f0724a044b5c9502ea853fe0886',
    '9ZW4_2132_atarget':r'1',
    '9ZW4_2132_forum_lastvisit':r'D_211_1433650915',
    '9ZW4_2132_visitedfid':r'211D136',
    '9ZW4_2132_connect_not_sync_t':r'1',
    '9ZW4_2132_sendmail':r'1',
    '9ZW4_2132_st_p':r'52909%7C1433651053%7Ca78e20339f1c5de0ecd236310a5738db',
    '9ZW4_2132_viewid':r'tid_35089',
    '9ZW4_2132_sid':r'fhnEzQ',
    '9ZW4_2132_check_key':r'',
    '9ZW4_2132_check_address':r'',
    '9ZW4_2132_smile':r'1D1',
    'Hm_lvt_380af268ee96366fb16c2e30f4b0fd3a':r'1432911617',
    'Hm_lpvt_380af268ee96366fb16c2e30f4b0fd3a':r'1433651037',
    '9ZW4_2132_noticeTitle':r'1',
    '9ZW4_2132_lastact':r'1433651067%09forum.php%09misc',
    '9ZW4_2132_connect_is_bind':r'0'
}

url = 'http://www.element3ds.com/forum.php?mod=post&action=reply&comment=yes&tid=35089&pid=730613&extra=&page=11&commentsubmit=yes&infloat=yes&inajax=1'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

payload = {'formhash': 'e54e456d', 'handlekey': 'comment', 'message': 'kankan', 'commentsubmit': 'true'}

count = 0
while(True):
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES, timeout=150)
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
    time.sleep(185)
