# -*- coding=UTF-8 -*-

import requests
import time
import sys
import json

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

# code = '7zt6'
# code = 'w0u1'
code = 'lkk6'

print base36decode(code)
# 370000
print pad(base36encode(373002))