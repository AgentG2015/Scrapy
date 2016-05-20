# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS = {
    'Host': 'www.cgdream.com.cn',
    'Connection': 'keep-alive',
    'Content-Length': '69',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.cgdream.com.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.cgdream.com.cn/forum.php?mod=viewthread&tid=264509&extra=page%3D1%26filter%3Dreply%26orderby%3Dreplies&page=11',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    'Hm_lvt_fc610018c4f88becba4f4f098bd24a48':r'1431786412,1431786489,1431787203,1431791120',
    'Hm_lpvt_fc610018c4f88becba4f4f098bd24a48':r'1433245018',
    'bdshare_firstime':r'1434613496108',
    'aKPx_2132_saltkey':r'PsS8KnRG',
    'aKPx_2132_lastvisit':r'1435924202',
    'aKPx_2132_tou_not_allow':r'd92cv%2FZlpcGLdn%2FkVZFRgA%2BasrNcbJsUGQrTGjMpPztgVZAjPyFIs7T9KuFcENMydjtmGqzQw3kSgy5zWH8zr9YU1OadcZER2f8okw',
    'aKPx_2132_ulastactivity':r'a18a8TVAwNI%2Bs%2BiXB97PE2YMJzy9W9YqEnoaCQ%2Fil5fX6SX%2FMzUJ',
    'aKPx_2132_auth':r'4b81%2FaPF8lzHWT4dopB%2BMHSn2rS98245dznGZMwG0j8DAeCn7QKXttmxiB4ehuqTGg10YxvRghBc%2BqQ6Q7JBjCz1Bv4',
    'aKPx_2132_security_cookiereport':r'2e065xZZG9oXmjjt0UC8ahN3cOJJIaiFj2oL5Gkg9qXCZvMPQUwk',
    'aKPx_2132_lip':r'115.174.156.177%2C1435927873',
    'aKPx_2132_nofavfid':r'1',
    'aKPx_2132_atarget':r'1',
    'tjpctrl':r'1435931959077',
    'aKPx_2132_home_diymode':r'1',
    'aKPx_2132_sendmail':r'1',
    'aKPx_2132_visitedfid':r'249D81D299D65D39',
    'aKPx_2132_st_t':r'381171%7C1435930309%7Cbd35b1546fef8ca33c09927337fb9c3c',
    'aKPx_2132_forum_lastvisit':r'D_65_1435930177D_299_1435930213D_81_1435930255D_249_1435930309',
    'aKPx_2132_st_p':r'381171%7C1435930319%7C41e96abc8432b664fe1259e37e60aeba',
    'aKPx_2132_viewid':r'tid_264509',
    'aKPx_2132_sid':r'zhiJ7c',
    'aKPx_2132_check_key':r'',
    'aKPx_2132_check_address':r'',
    'pgv_pvi':r'9304774563',
    'pgv_info':r'ssi=s7215202785',
    'aKPx_2132_smile':r'1D1',
    'aKPx_2132_lastact':r'1435930371%09forum.php%09ajax',
    'aKPx_2132_connect_is_bind':r'0'
}

url = 'http://www.cgdream.com.cn/forum.php?mod=post&action=reply&comment=yes&tid=264509&pid=1781078&extra=page%3D1%26filter%3Dreply%26orderby%3Dreplies&page=11&commentsubmit=yes&infloat=yes&inajax=1'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

payload = {'formhash': 'f8069346', 'handlekey': 'comment', 'message': 'kankan', 'commentsubmit': 'true'}

count = 0
while(True):
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES, timeout=600)
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
    time.sleep(4800)
