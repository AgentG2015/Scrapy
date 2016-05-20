# -*- coding=UTF-8 -*-

import re
import base64
import win32clipboard
import requests
    
HEADERS={
    'Host': 'www.cgboo.com',
    'Connection': 'keep-alive',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://www.cgboo.com/forum.php?mod=viewthread&tid=4749&extra=page%3D41%26filter%3Dsortid%26orderby%3Dlastpost%26sortid%3D12',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES={
    'PHPSESSID':r'4c66545fb148ba68fd79590dc9e659bf',
    'bdshare_firstime':r'1432147035255',
    'Wh0K_2132_saltkey':r'Yamhb7Am',
    'Wh0K_2132_lastvisit':r'1432218642',
    'Wh0K_2132_auth':r'261eG2fScBL96In2ykdck1Ice5u4Rd0k8OO4GOtHvnE4xlL0B6%2FjaD%2B04eI0ag0h5ccSM4POtyaY9qk1BJfacHi0%2FEs',
    'Wh0K_2132_lastcheckfeed':r'201260%7C1432278537',
    'Wh0K_2132_home_diymode':r'1',
    'Wh0K_2132_space_top_credit_201260_2':r'9419',
    'Wh0K_2132_atarget':r'1',
    'Wh0K_2132_security_cookiereport':r'07fdkYNStyjabN1NkPIUcjojrYITiDFiCeJkcJVctXx53AgdFbHK',
    'Wh0K_2132_nofavfid':r'1',
    'Wh0K_2132_ulastactivity':r'a94619Ne635f6Y2%2BfT3kvWmot7xVPZ2ekqwd%2FCefPpNQEYuPufDJ',
    'Wh0K_2132_st_t':r'201260%7C1432693503%7Ca16867daa1f6ea70484b3b099b8206b0',
    'Wh0K_2132_forum_lastvisit':r'D_62_1432663072D_60_1432663892D_65_1432664138D_125_1432664170D_126_1432664171D_122_1432664172D_121_1432664238D_123_1432664308D_124_1432664407D_48_1432665336D_79_1432693491D_47_1432693503',
    'Wh0K_2132_connect_not_sync_t':r'1',
    'pgv_pvi':r'9378774878',
    'pgv_info':r'ssi=s281103628',
    'Wh0K_2132_smile':r'1D1',
    'tjpctrl':r'1432696930023',
    'Wh0K_2132_lip':r'115.174.145.23%2C1432694929',
    'Wh0K_2132_lastact':r'1432696908%09forum.php%09viewthread',
    'Wh0K_2132_connect_is_bind':r'0',
    'Wh0K_2132_st_p':r'201260%7C1432696908%7Ce486525f569bc3d143be0b0e264a1cc8',
    'Wh0K_2132_visitedfid':r'47D79D64D60D48D123D65D156D129D62',
    'Wh0K_2132_viewid':r'tid_4749',
    'Wh0K_2132_sid':r'k4E58Y'
}
    
def get_hostname(url):
    from urlparse import urlparse
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain    
    
def download_file(url):
    # NOTE the stream=True parameter
    r = requests.get(url, headers=HEADERS, cookies=COOKIES, stream=True)
    print r
    find_list = re.findall('filename="(.*)"', r.headers["content-disposition"])
    local_filename = find_list[0] if len(find_list) > 0 else "hehe.zip"
    with open(local_filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

#get url_attachpay from windows clipboard
win32clipboard.OpenClipboard()
url_attachpay = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

#if "aid=\d+" then only one group: the whole match, if "aid=(\d+)" then two groups, first being the whole match, second the string in between braces
aid = re.search("aid=(\d+)", url_attachpay).group(1)
tid = re.search("tid=(\d+)", url_attachpay).group(1)

aid_unencrypted = "%s|37aad6a9|1432140672|1|%s" % (aid, tid)
aid_encrypted = base64.b64encode(aid_unencrypted)

url = r"%sforum.php?mod=attachment&aid=%s" % (get_hostname(url_attachpay), aid_encrypted)
print url

download_file(url)
