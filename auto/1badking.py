# -*- coding=UTF-8 -*-

from gevent import monkey
monkey.patch_all()

import requests
import os
import time
import codecs

from lxml import html
import gevent

folder = 'bk/'

HEADERS = {
    'Host': 'www.badking.com.au',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Referer': 'http://www.badking.com.au/site/checkout/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    'wordpress_test_cookie':r'WP+Cookie+check',
    'wordpress_logged_in_3dac4fcd2343afbadac027d43ceed82e':r'AgentK%7C1437811538%7CQTBvxfUAEZq60eOl5mXS8KDz168tkyMQJydoT47Wjiq%7C6bcc641fb6e404304a5f44758e20dd8084c63b5d08bbee8fed24c5df7543345a',
    'woocommerce_recently_viewed':r'10882%7C10896%7C3622%7C3627%7C3659%7C3628%7C3631%7C3694%7C3720%7C3547%7C3721%7C3580%7C3581%7C3587%7C3588',
    'wp_woocommerce_session_3dac4fcd2343afbadac027d43ceed82e':r'49709%7C%7C1436775006%7C%7C1436771406%7C%7Cd06f85ac1583c70ea857a38527fc0ae6',
    'act_logged':r'1436601938',
    'PHPSESSID':r'5772c14d90e96b1b193017a14963a1b1'
}

url = 'http://www.badking.com.au/site/checkout/order-received/106221/?key=wc_order_55a14541b1799'

def silce_iter(in_list, slice_count=998):
    start_index = 0
    end_index = slice_count
    while end_index <= len(in_list):
        yield in_list[start_index:end_index]
        start_index += slice_count
        end_index += slice_count
    if len(in_list) > start_index:
        yield in_list[start_index:]

def fetch_all(node):
    # get field
    name = node.xpath('a/text()')[0]
    rindex = name.lower().rfind(' by ')
    if rindex > 0:
        name = name[:rindex]

    pic_html_url = node.xpath('a/@href')[0]
    zip_url_list = node.xpath('small/a/@href')

    # get pic
    r = requests.get(pic_html_url, timeout=60)
    pic_url = html.fromstring(r.text).xpath('//img[@id="main-image"]/@src')[0]
    r = requests.get(pic_url, timeout=60)
    pic_filename = folder + name + '.jpg'
    with open(pic_filename, 'wb') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)

    # get zip
    if len(zip_url_list) == 1:
        zip_filename = folder + name + '.zip'
        r = requests.get(zip_url_list[0], headers=HEADERS, cookies=COOKIES, timeout=60)
        with open(zip_filename, 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
    else:
        for zip_index, zip_url in enumerate(zip_url_list):
            zip_filename = folder + name + '_' + str(zip_index + 1) + '.zip'
            r = requests.get(zip_url, headers=HEADERS, cookies=COOKIES, timeout=60)
            with open(zip_filename, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)

if __name__ == '__main__':
    stime = time.time()
    with codecs.open('1.html', 'r', 'utf-8') as f:
        text = f.read()

    tree = html.fromstring(text)
    nlist = tree.xpath('//*[@id="page-content-wrapper"]/div[1]/div/table[2]/tbody/tr/td[1]')
    for i, sliced_list in enumerate(silce_iter(nlist, 5)):
        if not 36 < i <= 37:
            continue
        threads = []
        for node in sliced_list:
            threads.append(gevent.spawn(fetch_all, node))
        gevent.joinall(threads)
    print '%.2fs' % (time.time() - stime)
