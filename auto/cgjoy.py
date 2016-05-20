# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS = {
    'Host': 'www.cgjoy.com',
    'Connection': 'keep-alive',
    'Content-Length': '181',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.cgjoy.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.cgjoy.com/forum.php?mod=viewthread&tid=62345&extra=page%3D1%26filter%3Dreply%26orderby%3Dreplies&page=11',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    'gCpn_2132_saltkey':r'Y18q0Cjm',
    'gCpn_2132_lastvisit':r'1432143438',
    'gCpn_2132_lastcheckfeed':r'313322%7C1432147642',
    'gCpn_2132_auth':r'0f62C13863K891R7f2N3NgNVteHLrs7LkWjE5tEpuOvrsdBU%2FfRuwY6l3U0y9A0Dq%2BLGT63XtyuX7Nm%2BWEmXP2yXvY4',
    'gCpn_2132_nofavfid':r'1',
    'gCpn_2132_pc_size_c':r'1bdcfae',
    'gCpn_2132_atarget':r'1',
    'Hm_lvt_bb326907b27f8f936619c43d1855729a':r'1432912717',
    'Hm_lpvt_bb326907b27f8f936619c43d1855729a':r'1432912717',
    'bdshare_firstime':r'1432912716729',
    'IESESSION':r'alive',
    'gCpn_2132_security_cookiereport':r'a1a71Wy9KW%2BezNMv9kQcgywe5rALNu2ypt8cPfZfN6DI6HljMGlu',
    'gCpn_2132_ulastactivity':r'a8a7D9QQ9Zwf50t47liYLZq53wu6FqfPi31IBF1H%2FQ3k%2Fu1OGghy',
    'gCpn_2132_home_diymode':r'1',
    'gCpn_2132_seccodeSfGGZof0':r'eb2eXQnqOjbukiZIGQkakqQZ0FUhJ03qbFmLOVj5wRizfFl42aiNN5%2FUULlC8psz4g7lfj3GcKWei2wQr8o',
    'gCpn_2132_connect_not_sync_t':r'1',
    'a7562_times':r'2',
    'pgv_si':r's9553852416',
    'gCpn_2132_seccodeSxRnSNj0':r'590evoJGdeU8cblKxTi%2FjHnwps8Xvno5mw%2Fk2nocfhnLa80ybqrFuhGTdZBCVHPQlXVM%2F1vAuHSXGEsRnsE',
    'gCpn_2132_lip':r'183.129.129.190%2C1433165554',
    'gCpn_2132_sendmail':r'1',
    'tjpctrl':r'1433173099716',
    'gCpn_2132_visitedfid':r'226D114D91D115D199',
    'gCpn_2132_forum_lastvisit':r'D_199_1433155077D_226_1433171448',
    'gCpn_2132_checkpm':r'1',
    'gCpn_2132_viewid':r'tid_62345',
    'pgv_pvi':r'7837846064',
    'pgv_info':r'ssi=s5625551964',
    'AJSTAT_ok_pages':r'21',
    'AJSTAT_ok_times':r'18',
    'CNZZDATA2571762':r'cnzz_eid%3D2049457742-1432143584-null%26ntime%3D1433170563',
    'gCpn_2132_sid':r'XD75sl',
    'gCpn_2132_smile':r'2D1',
    'gCpn_2132_lastact':r'1433171465%09forum.php%09misc',
    'gCpn_2132_connect_is_bind':r'0'
}

url = 'http://www.cgjoy.com/forum.php?mod=post&action=reply&comment=yes&tid=62345&pid=2179749&extra=page%3D1%26filter%3Dreply%26orderby%3Dreplies&page=11&commentsubmit=yes&infloat=yes&inajax=1'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

payload = {'formhash': 'c35c407c', 'handlekey': 'comment', 'message': 'kankan', 'commentsubmit': 'true'}

count = 0
while(True):
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES, timeout=60)
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
    time.sleep(1801)
