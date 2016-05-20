# -*- coding=UTF-8 -*-

from gevent import monkey
monkey.patch_all()

import os
import sys
import time
import requests
from requests.exceptions import ConnectionError
from gevent.pool import Pool

step = 10000
start = 10000000
end = 10100000
# end = 20000000
max_retry_count = 100
pool_size = 900

uk = '3544613589'
# shareid = 747989750
url_tpl = 'http://pan.baidu.com/share/init?shareid=%s&uk=' + uk

res_folder = 'res/'
list_200 = 'list_200.txt'
list_302 = 'list_302.txt'
list_max = 'list_max.txt'
list_others = 'list_others.txt'

def sc_worker(s, url):
    retry_count = 0
    while retry_count < max_retry_count:
        try:
            r = s.head(url, allow_redirects=False, stream=False)
        except ConnectionError as e:
            retry_count += 1        
            continue
        except Exception as e:
            raise e
        else:
            if r.status_code == 302:
                if r.headers['Location'] != 'http://pan.baidu.com/error/404.html':
                    file_302.write(r.headers['Location'] + '\n')
                    file_302.flush()
            elif r.status_code == 200:
                file_200.write(r.url + '\n')
                file_200.flush()
            else:
                file_others.write(r.status_code + '\t' + r.url + '\n')
                file_others.flush()
            break
    else:
        file_max.write(url + '\n')
        file_max.flush()
        
if __name__ == "__main__":
    start_time = time.time()
    
    # init
    if not os.path.exists(res_folder):
        os.makedirs(res_folder)
    file_200 = open(res_folder + list_200, 'w')
    file_302 = open(res_folder + list_302, 'w')
    file_max = open(res_folder + list_max, 'w')
    file_others = open(res_folder + list_others, 'w')
    
    # requests
    s = requests.Session()
    pool = Pool(pool_size)  
    for i in xrange(start, end):
        if i % step == 0:
            print '%i/%i' % (i, end)
            sys.stdout.flush()
        shareid = i
        url = url_tpl % shareid
        pool.spawn(sc_worker, s, url)
    pool.join()
        
    # finalize
    file_200.close()
    file_302.close()
    file_max.close()
    file_others.close()
    
    elapsed_time = time.time() - start_time
    print '%.2fs, %.2f pages/min' % (elapsed_time, 100000 / elapsed_time * 60)
     