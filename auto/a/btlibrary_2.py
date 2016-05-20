# -*- coding=UTF-8 -*-

from lxml import html
import logging
import requests

# not used, maybe useful sometime, so keep it here for now
HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

try:
    tor_host = 'http://storebt.com'
    url_1 = 'http://btlibrary.org/torrent/69197341814037d8fcc0695cba211013b2646d3a/Ariel-Exotic-Cocos-WowGirls-2013-HD-iyutero-com-mp4.html'

    r_1 = requests.get(url_1, timeout=10)
    tree_1 = html.fromstring(r_1.text)
    url_2 = tree_1.xpath('/html/body/div[1]/div[2]/div/div/table/tr[10]/td[2]/a[2]/@href')[0]
    print url_2

    r_2 = requests.get(url_2, timeout=10)
    tree_2 = html.fromstring(r_2.text)
    url_3 = tor_host + tree_2.xpath('/html/body/div[1]/a/@href')[0]
    print url_3

    filename = url_3.split('/')[-1]
    r_3 = requests.get(url_3, timeout=10)

    with open(filename, 'wb') as f:
        for chunk in r_3.iter_content(1024):
            f.write(chunk)
except Exception as e:
    logging.exception('Error:\n')
    raw_input('')