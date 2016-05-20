# -*- coding=UTF-8 -*-

from gevent import monkey
monkey.patch_all()

import requests
import json
import os
import time

import gevent

zip_url_temp = 'http://download.pixologic01.com/download.php?f=/library/'
img_url_temp = 'http://pixologic.com/zbrush/downloadcenter/alpha/images/'

HEADERS = {
    'Host': 'download.pixologic01.com',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Referer': 'http://pixologic.com/zbrush/downloadcenter/alpha/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language: zh-CN,zh;q':r'0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

def silce_iter(in_list, slice_count=998):
    start_index = 0
    end_index = slice_count
    while end_index <= len(in_list):
        sliced_list = in_list[start_index:end_index]
        start_index += slice_count
        end_index += slice_count
        yield sliced_list
    if len(in_list) > start_index:
        yield in_list[start_index:]

def fetch_all(img_url, zip_url):
    filename = os.path.basename(img_url_temp + img_url)
    r = requests.get(img_url_temp + img_url, timeout=60)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    filename = os.path.basename(zip_url_temp + zip_url)
    r = requests.get(zip_url_temp + zip_url, headers=HEADERS, timeout=60)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

if __name__ == '__main__':
    stime = time.time()
    url = 'http://pixologic.com/zbrush/downloadcenter/alpha/getLibrary.php?n=0'
    r = requests.get(url, timeout=10)
    j = json.loads(r.text)

    for sliced_list in silce_iter(j, slice_count=5):
        threads = []
        for item in sliced_list:
            threads.append(gevent.spawn(fetch_all, item['thumbnail'], item['link']))
        gevent.joinall(threads)
    print '%.2fs' % (time.time() - stime)
