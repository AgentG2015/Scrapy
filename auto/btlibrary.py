# -*- coding=UTF-8 -*-

from lxml import html
import requesocks as requests

# not used, maybe useful sometime, so keep it here for now
HEADERS = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Referer': 'http://btlibrary.org/b/K8kvScxRKEmtKCktSi1WKDNUKDICAA.html',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

def get_clipboard():
    import win32clipboard
    win32clipboard.OpenClipboard()
    ret = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return ret

try:
    proxies = {'http': 'socks5://127.0.0.1:8090', 'https': 'socks5://127.0.0.1:8090'}
    tor_host = 'http://storebt.com'
    url_1 = get_clipboard()

    r_1 = requests.get(url_1, proxies=proxies, timeout=10)
    tree_1 = html.fromstring(r_1.text)
    url_2 = tree_1.xpath('/html/body/div[1]/div[2]/div/div/table/tr[10]/td[2]/a[2]/@href')[0]

    r_2 = requests.get(url_2, proxies=proxies, timeout=10)
    tree_2 = html.fromstring(r_2.text)
    url_3 = tor_host + tree_2.xpath('/html/body/div[1]/a/@href')[0]

    filename = url_3.split('/')[-1]
    r_3 = requests.get(url_3, proxies=proxies, timeout=10)

    with open(filename, 'wb') as f:
        for chunk in r_3.iter_content(1024):
            f.write(chunk)
except Exception as e:
    raw_input('Exception: ' + str(e))