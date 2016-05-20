# -*- coding=UTF-8 -*-

import requests
import time
import sys
import codecs
from lxml import html
import base64
import subprocess

HEADERS_1 = {
    'Host': 'upsto.re',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Referer': 'http://downl.ink/f35f16',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES_1 = {
    '__cfduid':r'd2386d08b45ed1d48552c188bece300cc1434119332'
}

HEADERS_2 = {
    'Host': 'upstore.net',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Referer': 'http://downl.ink/f35f16',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES_2 = {
    '__cfduid':r'dd2cf4084d938e3f9e0397252de6eea6a1434119329',
    'lang':r'en',
    'last':r'gxgwUC',
    'r':r'54639',
    'upst':r'6g5r6hlh8qj3j31slktic7cdd0',
    'usid':r'1168iETqkSaHvjYLisQwj8VNtLfXXJ66PskY',
    'ref':r'http%3A%2F%2Fdownl.ink%2Ff35f16'
}

url = 'http://downl.ink/ee24c6'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

r = requests.get(url, timeout=10)
tree = html.fromstring(r.text)
script = tree.xpath('//script/text()')[0].split('\n')

script_unchanged = script[:-2]
script_base64 = script[-2][11:-4]

script_decoded = base64.b64decode(script_base64)
script_modefied = script_decoded.split('\n')[:-2]
last_line = script_modefied[-1]

script_modefied.append('process.stdout.write(%s)' % last_line[:6])

with codecs.open('decoded.txt', 'w', 'utf-8') as f:
    for line in script_unchanged:
        f.write(line + '\n')
    for line in script_modefied:
        f.write(line + '\n')
    
node_cmd = 'node decoded.txt'
result = subprocess.Popen(node_cmd, shell=True, stdout=subprocess.PIPE)
url2 = result.stdout.readlines()[0]

print url2

r2 = requests.get(url2, headers = HEADERS_1, cookies = COOKIES_1, allow_redirects=False, timeout=10)

url3 = r2.headers['location']

r3 = requests.get(url3, headers = HEADERS_2, cookies = COOKIES_2, allow_redirects=False, timeout=10)

ret = r3.headers['location']

print ret
    

