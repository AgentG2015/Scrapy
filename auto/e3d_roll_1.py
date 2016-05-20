# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS = {
    'Host': 'www.element3ds.com',
    'Connection': 'keep-alive',
    'Content-Length': '65',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.element3ds.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.element3ds.com/plugin.php?id=yinxingfei_zzza:yinxingfei_zzza_hall',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    '9ZW4_2132_saltkey':r'gNxv1Nu9',
    '9ZW4_2132_lastvisit':r'1433063407',
    '9ZW4_2132_ulastactivity':r'4190rktQA9LexJ3Z%2ByoyWd7nV2PAoZwQRrGAGBPfH1kMZWE%2FMc4q',
    '9ZW4_2132_auth':r'8e57uzWRPpwL%2B6f3kfLw399hQSOnj3akdjgfMNWOh9gw0rW3Cmcg6NNuJi%2Bc5ZZ%2B6Gj%2FeicZjdblFoko4uZPRTb4Ng',
    '9ZW4_2132_taskdoing_51718':r'1',
    '9ZW4_2132_nofavfid':r'1',
    '9ZW4_2132_atarget':r'1',
    '9ZW4_2132_forum_lastvisit':r'D_133_1433067204D_154_1433067239D_153_1433067243',
    '9ZW4_2132_st_t':r'51718%7C1433068414%7C87db31b8b9f41bde263f8c413774db36',
    '9ZW4_2132_connect_not_sync_t':r'1',
    '9ZW4_2132_lip':r'221.11.109.98%2C1433067050',
    '9ZW4_2132_st_p':r'51718%7C1433077296%7C2fb132930eb2ede8054c3345ffa9c6fb',
    '9ZW4_2132_visitedfid':r'263D153D132D154D211D133',
    '9ZW4_2132_viewid':r'tid_35548',
    '9ZW4_2132_check_key':r'',
    '9ZW4_2132_check_address':r'',
    '9ZW4_2132_smile':r'1D1',
    'tjpctrl':r'1433079673618',
    '9ZW4_2132_sendmail':r'1',
    '9ZW4_2132_sid':r'ZI5D1w',
    'Hm_lvt_380af268ee96366fb16c2e30f4b0fd3a':r'1432981833,1432983472,1432992118,1433054825',
    'Hm_lpvt_380af268ee96366fb16c2e30f4b0fd3a':r'1433077934',
    '9ZW4_2132_lastact':r'1433077952%09misc.php%09patch',
    '9ZW4_2132_connect_is_bind':r'0'
}

url = 'http://www.element3ds.com/plugin.php?id=yinxingfei_zzza:yinxingfei_zzza_post'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

#zzza_txt1=0&zzza_txt2=1&zzza_txt3=2&zzza_fw1=12
payload = {'formhash': '886b1a7d', 'zzza_txt1': '0', 'zzza_txt2': '1', 'zzza_txt3': '2', 'zzza_fw1': '40000'}

count = 0
while(True):
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES, timeout=150)
    except Exception as e:
        print e
        sys.stdout.flush()
        continue
    with open('hehe.html', 'w') as f:
        f.write(r.text.encode('gbk'))
    time.sleep(185)
