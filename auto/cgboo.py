# -*- coding=UTF-8 -*-

import requests
import time
import sys

HEADERS = {
    'Host': 'www.cgboo.com',
    'Connection': 'keep-alive',
    'Content-Length': '75',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Origin': 'http://www.cgboo.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://www.cgboo.com/forum.php?mod=viewthread&tid=13377&extra=page%3D1&page=12',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

COOKIES = {
    'PHPSESSID':r'4c66545fb148ba68fd79590dc9e659bf',
    'bdshare_firstime':r'1432147035255',
    'Wh0K_2132_saltkey':r'Yamhb7Am',
    'Wh0K_2132_lastvisit':r'1432218642',
    'Wh0K_2132_auth':r'261eG2fScBL96In2ykdck1Ice5u4Rd0k8OO4GOtHvnE4xlL0B6%2FjaD%2B04eI0ag0h5ccSM4POtyaY9qk1BJfacHi0%2FEs',
    'Wh0K_2132_lastcheckfeed':r'201260%7C1432278537',
    'Wh0K_2132_space_top_credit_201260_2':r'9419',
    'Wh0K_2132_atarget':r'1',
    'Wh0K_2132_nofavfid':r'1',
    'Wh0K_2132_con_request_uri':r'http%3A%2F%2Fwww.cgboo.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dhome.php%253Fmod%253Dspacecp%2526ac%253Dplugin%2526id%253Dqqconnect%253Aspacecp',
    'Wh0K_2132_client_created':r'1433061186',
    'Wh0K_2132_client_token':r'873D9B4D6ABE81CBE146B3B35BAF25E9',
    'Wh0K_2132_connect_login':r'1',
    'Wh0K_2132_connect_uin':r'873D9B4D6ABE81CBE146B3B35BAF25E9',
    'Wh0K_2132_connect_synpost_tip':r'1',
    'Wh0K_2132_security_cookiereport':r'42c1u16lBfcyO4oYQ5yuG7%2F09cwI8CIxwK%2BQ2znSrBRpQXwXa%2FgO',
    'Wh0K_2132_ulastactivity':r'2d5eMFtC5sXHRWipJkDyGM0OXf3W0JbE7M7SF4pe1X2wd9XnkSV%2B',
    'Wh0K_2132_lip':r'211.161.249.45%2C1433149992',
    'tjpctrl':r'1433155222083',
    'Wh0K_2132_st_t':r'201260%7C1433153510%7Cb4d6e420f030e6c2e979ebe74c8b8766',
    'Wh0K_2132_forum_lastvisit':r'D_62_1432663072D_60_1432663892D_65_1432664138D_125_1432664170D_126_1432664171D_122_1432664172D_121_1432664238D_123_1432664308D_124_1432664407D_48_1432665336D_47_1432701732D_46_1432711819D_145_1433127607D_37_1433127610D_150_1433148297D_79_1433153510',
    'Wh0K_2132_visitedfid':r'79D123D150D42D37D145D65D59D64D125',
    'Wh0K_2132_home_diymode':r'1',
    'Wh0K_2132_sendmail':r'1',
    'Wh0K_2132_connect_not_sync_feed':r'1',
    'Wh0K_2132_connect_not_sync_t':r'1',
    'Wh0K_2132_st_p':r'201260%7C1433153776%7C10f3633797c44611ad5fbad5e1c6e93a',
    'Wh0K_2132_viewid':r'tid_13377',
    'Wh0K_2132_sid':r'gVx8rz',
    'pgv_pvi':r'9378774878',
    'pgv_info':r'ssi=s281103628',
    'Wh0K_2132_smile':r'1D1',
    'Wh0K_2132_lastact':r'1433153810%09forum.php%09post',
    'Wh0K_2132_connect_is_bind':r'1'
}

url = 'http://www.cgboo.com/forum.php?mod=post&action=reply&comment=yes&tid=13377&pid=111800&extra=page%3D1&page=12&commentsubmit=yes&infloat=yes&inajax=1'

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]

payload = {'formhash': '6906b6d5', 'handlekey': 'comment', 'message': u'看看'.encode('gbk'), 'commentsubmit': 'true'}

count = 0
while(True):
    try:
        r = requests.post(url, data=payload, headers=HEADERS, cookies=COOKIES, timeout=10)
    except Exception as e:
        print e
        sys.stdout.flush()
        continue
    if u"帖子点评成功" in r.text:
        count += 1
        print "%s\t%i" % (filename, count)
        sys.stdout.flush()
    else:
        try:
            print r.text
        except:
            print "ascii error"
        sys.stdout.flush()
    time.sleep(0.1)
    