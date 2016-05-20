# -*- coding=UTF-8 -*-

import requests
import time
import json
import errno

HEADERS={
    'Host': 'vip.115.com',
    'Connection': 'keep-alive',
    'Content-Length': '59',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://vip.115.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://vip.115.com/order/mycoupon/?t=space&m=5120&c=1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES={
    '115_lang':r'zh',
    'PHPSESSID':r'ng14d3phkaomd0u1u0eedkfa07',
    'pgv_pvi':r'1982259200',
    'pgv_si':r's5222417408',
    'payment':r'115fengye',
    'UUID':r'11555549CB0D7B41',
    'UUTK':r'a2ef47NP%2FvrjAMg3PpphOdi7BzCxlkGF%2F1ishrvWrDuouKdDqXh2zLmMSgwfJGK7Jf0%2B3HJWHQGgssGpnkTBGq4tlxNqq1%2BF%2BDkaU',
    'loginType':r'0',
    'ssoidA1':r'5377738cffa4a15caabb7e4c5752aad858b87869',
    'ssoinfoA1':r'360723746%3AA1%3A1697393928',
    'OORA':r'684cec91c2d7a33601ba51d3b68ca6869ed85f7b',
    'OOFA':r'%2506%2501QQTQ%2506%2502%2501%250Dy%2505S%250CBy%2508%2502WP%250A%2504%2505U%250APSQY%255B%2509%2509%2506%2501XWUZ%2501T%2507%2505%255D%2504P%255B%250FQV%250AR%2500%2501%2504%2504%255C%2506%2504%2507S%2505%2503%2500W',
    'OOFV':r'9e0f67c71dea54d271b9adee5c71ce0cac03298823c72b98bb77e99c9d363e25a145ea65a87a8ea76e4e75e471165651',
    'UID':r'360723746_A1_1431608514',
    'CID':r'b110aba40e9c72c65b9d8b3989ea4a54',
    'SEID':r'b3101acadaca31943836bfb1c3e8b789fdacd0e1aeda9ad800847c39fdf2a58e4d6e26695b6e8dd31150d3a6687c0dc77e71d6b58998b5bb0b6c2353',
    'OOFL':r'2358411799%40qq.com',
    'ssov_360723746':r'1_360723746_e7ca3a79db8b417d4c62e764a146f3de',
    '__utmt':r'1',
    '__utma':r'48116967.1466479586.1418891680.1419128987.1431608545.3',
    '__utmb':r'48116967.1.10.1431608545',
    '__utmc':r'48116967',
    '__utmz':r'48116967.1418891680.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    'PAY_WAP':r'0',
    'PAY_MIN':r'0',
}

url = r"https://vip.115.com/?ct=order&ac=coupon&t=space&is_ajax=1&n=";
user_start = 326140385
count = 100000

cards = []
with open("cards.txt", 'r') as f:
    cards = f.read().split("\n")

user_index = 0
card_index = 0
cards_count = len(cards)

while(True):   
    payload = {'coupon': '%s' % (cards[card_index]), 'user': '%i' % (user_start + user_index), 'vcode': 'xhrk', 'is_ajax': '1'}
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES)
    except requests.exceptions.ConnectionError as e:
        continue
    result = json.loads(r.text)   
    print "prog:\t%i/%i" % (card_index, cards_count)
    print "user:\t%i" % (user_start + user_index)
    print "state:\t%s" % result["state"]
    print "body:\t%s" % result["body"]
    print "-----------------------------------------------------------------------"
    if len(result["state"]) == 0:
        card_index += 1
        user_index -= 1
    if u"已在" in result["body"]:
        card_index += 1
        user_index -= 1
    if card_index >= cards_count:
        print "Done! Congratulations!"
        break
    user_index += 1
    if user_index >= count:
        print "Count reaches limit! Current card: %s, %i/%i" % (cards[card_index], card_index, cards_count)
        break
    time.sleep(0.1)
    
