# -*- coding=UTF-8 -*-

import requests
import json
import os
import codecs

def get_clipboard():
    import win32clipboard
    win32clipboard.OpenClipboard()
    ret = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return ret


def set_clipboard(data):
    import win32clipboard
    win32clipboard.OpenClipboard()
    # important, must empty clipboard first, otherwise it won't work
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(data)
    win32clipboard.CloseClipboard()


'''
CONNECT kharma.unity3d.com:443 HTTP/1.1
Host: kharma.unity3d.com:443
Proxy-Connection: Keep-Alive
Origin: https://kharma.unity3d.com
X-Kharma-Version: 5.1.0-r84289                          # must                                                            
X-Unity-Session: XJ2xSdotFbwXU0ooetH                    # must
X-Requested-With: UnityAssetStore
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Unity/4.6.3f1 (http://unity3d.com)
Accept: */*
Referer: https://kharma.unity3d.com/en/
'''

HEADERS = {
    'Host': 'kharma.unity3d.com',
    'Connection': 'Keep-Alive',
    'X-Kharma-Version': '5.2.0-r85615',
    'X-Unity-Session': 'ku2qGtYGGbS1T40fkuztENPrEsfk1KKHYNq2ffG-myTCI9D-fldVRv67jWDqpCefGdLVajhfcS_buuRLQsjvjg::Sausage::',
    'X-Requested-With': 'UnityAssetStore',
    'User-Agent': 'Mozilla/5.0 (Windows; Win64; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 Safari/537.36Unity/5.1.1f1 (unity3d.com)',
    'Accept': '*/*',
    'Referer': 'https://kharma.unity3d.com/en/',
}

COOKIES = {
    'unity_version': '5.1.1f1',
    'unity_version_full': '5.1.1f1 (2046fc06d4d8)',
    'SERVERID': 'varnish01',
    'kharma_explicitly_logged_out': '0'
}


try:
    url_template = 'https://kharma.unity3d.com/api/en-US/content/download/%s.json'
    json_id = get_clipboard().split('/')[-1]
    url = url_template % json_id
    print url

    r = requests.get(url, headers=HEADERS, timeout=30)
    print r.text
    j = json.loads(r.text)

    '''
    {
        "download": {
            "link": {
                "id": "22755",
                "type": "content"
            },
            "progress": "100",
            "filename_safe_package_name": "Painterly Nature",
            "key": "bc102e2a499103433e3bf4cd69769c94ccac89c78ec482160d97c17ce2728ff6e12a2e00da6b2c01d70ee120e4340acd",
            "filename_safe_category_name": "3D ModelsEnvironmentsFantasy",
            "url": "http://assetstore.unity3d.com.s3.amazonaws.com/download/5ff07f6c-5a49-4735-8de1-496d6c06551f",
            "filename_safe_publisher_name": "Shapes",
            "id": "22755"
        }
    }
    '''

    url = j['download']['url']
    filename_safe_package_name = j['download']['filename_safe_package_name']
    set_clipboard(url)
    filename = url.split('/')[-1] + '_' + filename_safe_package_name + '.txt'
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(json.dumps(j, sort_keys=True, indent=4, separators=(',', ': ')))
except Exception as e:
    raw_input('Exception: ' + str(e))