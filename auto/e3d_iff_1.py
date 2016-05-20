# -*- coding=UTF-8 -*-

import requests
import requesocks
import time

HEADERS={
    'Host': 'www.element3ds.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'
}

filename = __file__
rindex = filename.rfind('\\')
if rindex >=0:
    filename = filename[rindex+1:-3]
    
start_index = 1
timeout = 3
max_retry_count = 3
max_iterate_count = 200
max_response_time = 5000        #unit = milliseconds

#read proxies from file    
httpList = []    
socks5List = []
with open('http.txt', 'r') as f:
    lines = f.read().split("\n")
    for line in lines:
        if len(line) == 0:
            continue
        httpList.append(line.split("\t"))
with open('socks5.txt', 'r') as f:
    lines = f.read().split("\n")
    for line in lines:
        if len(line) == 0:
            continue
        socks5List.append(line.split("\t"))

url = r"http://www.cgboo.com/forum.php?mod=viewthread&tid=14976";
proxies = {}
#format: {"http": "http://162.248.247.167:1080"}

#begin iff
iterate_count = 0
ip_count = len(httpList)
failed_ip = 0
for i, proxy in enumerate(httpList):
    if i < start_index - 1:
        continue
    if int(proxy[4]) > max_response_time:
        print "Max response time reached: %s" % max_response_time
        break
        
    print "-------------------------------------------------------------"
    print "iterate: %i/%i, ip_count: %i/%i, failed_ip: %i, ms: %s" % (iterate_count+1, max_iterate_count, i+1, ip_count, failed_ip, proxy[4])
    proxyStr = "http://%s:%s" % (proxy[0], proxy[1])
    proxies["http"] = proxyStr
    
    retry_count = 0
    while retry_count < max_retry_count:
        try:
            r = requests.get(url, headers=HEADERS, proxies=proxies, timeout=timeout)
        except Exception as e:
            print e
            retry_count += 1            
            continue
        break
    
    if retry_count >= max_retry_count:
        failed_ip += 1
    else:
        print r.status_code
        if r.status_code != 200:
            failed_ip += 1
        else:
            iterate_count += 1
            if iterate_count >= max_iterate_count:
                print "Max iterate count reached: %s" % max_iterate_count
                break