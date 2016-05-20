# -*- coding=UTF-8 -*-

import requests
import time
import sys
import codecs

HEADERS = {
    'Host': 'weibo.cn',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
    'Referer': 'http://login.sina.com.cn/sso/login.php?url=http%3A%2F%2Fweibo.cn%2F&_rand=1459773318.0376&gateway=1&service=sinawap&entry=sinawap&useticket=1&returntype=META&sudaref=&_client_version=0.6.16',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    '_T_WM': 'fdae26fda9a82e2666d18d4d0750b947',
    'WEIBOCN_WM': '3333_2001',
    'SUB': '_2A256Bi_WDeTxGeNJ6VQV8yfKzj2IHXVZCLGerDV6PUJbstBeLWrDkW1LHet9cPK1GkuH_-hcJEf14KmpwMKFvg..',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhriXTA58-A3E.bWgTqXro65JpX5o2p',
    'SUHB': '0auQgVskoji9Ag',
    'SSOLoginState': '1459773318',
    'gsid_CTandWM': '4uNxCpOz5QSp0B0OzkkJDo1HVav'
}

url = 'http://weibo.cn/'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

r = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=60)
with codecs.open('weibo.html', 'w', 'utf-8') as f:
    f.write(r.text)