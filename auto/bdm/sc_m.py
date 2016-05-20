# -*- coding=UTF-8 -*-

from gevent import monkey
monkey.patch_all()

import os
import time
import sqlite3
import requests
import multiprocessing as mp
from requests.exceptions import ConnectionError
from gevent.pool import Pool

step = 10000
start = 100000000
end = 101000000

max_retry_count = 100
pool_size = 72
p_count = 8

uk = '3544613589'
url_tpl = 'http://pan.baidu.com/share/init?shareid=%s&uk=' + uk

res_folder = 'res/'
list_200_pre = 'list_200_'
list_302_pre = 'list_302_'
list_max_pre = 'list_max_'
list_others_pre = 'list_others_'
list_log_pre = 'list_log_'
file_ext = '.txt'

db_location = 'sc.sqlite3'

def db_insert(shareid, url):
    conn = sqlite3.connect(db_location)
    c = conn.cursor()
    sql = "insert into sc (shareid, uk, url) values (%s, %s, '%s')" % (shareid, uk, url)
    c.execute(sql)
    conn.commit()
    conn.close()

def sc_worker(pid, s, shareid, url, file_list):
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
                    file_list[1].write(r.headers['Location'] + '\n')
                    file_list[1].flush()
            elif r.status_code == 200:
                file_list[0].write(r.url + '\n')
                file_list[0].flush()
                # insert into table
                db_insert(shareid, url)
            else:
                file_list[3].write(r.status_code + '\t' + r.url + '\n')
                file_list[3].flush()
            break
    else:
        file_list[2].write(url + '\n')
        file_list[2].flush()

def sc_process(pid, p_start, p_end):
    # init 
    file_200 = open(res_folder + list_200_pre + str(pid) + file_ext, 'w')
    file_302 = open(res_folder + list_302_pre + str(pid) + file_ext, 'w')
    file_max = open(res_folder + list_max_pre + str(pid) + file_ext, 'w')
    file_others = open(res_folder + list_others_pre + str(pid) + file_ext, 'w')
    file_log = open(res_folder + list_log_pre + str(pid) + file_ext, 'w')
    file_list = [file_200, file_302, file_max, file_others, file_log]

    s = requests.Session()
    pool = Pool(pool_size) 
    for i in xrange(p_start, p_end):
        if i % step == 0:
            file_log.write('%i/%i\n' % (i, p_end))
            file_log.flush()
        shareid = i
        url = url_tpl % shareid
        pool.spawn(sc_worker, pid, s, shareid, url, file_list)
    pool.join()
    
    # finalize
    file_200.close()
    file_302.close()
    file_max.close()
    file_others.close()
    file_log.close()

def merge_files(file_pre):
    file_list = [f for f in os.listdir(res_folder) if file_pre in f]
    lines = []
    for f in file_list:
        with open(res_folder + f, 'r') as fd:
            tmp = fd.read().strip()
            if len(tmp) != 0:
                lines.extend(tmp.split('\n'))
        os.remove(res_folder + f)
    if len(lines) > 0:
        with open(res_folder + file_pre[:-1] + file_ext, 'w') as f:
            for line in lines:
                f.write(line + '\n')

def main():
    start_time = time.time()

    # init
    if not os.path.exists(res_folder):
        os.makedirs(res_folder)
    # delete all file first
    for f in os.listdir(res_folder):
        os.remove(res_folder + f)

    p_step = (end - start) / p_count
    processes = []
    for pid in range(p_count):
        p_start = start + pid * p_step
        p_end = p_start + p_step
        p = mp.Process(target=sc_process, args=(pid, p_start, p_end))
        processes.append(p)

    for p in processes:
        p.start()
        time.sleep(5)

    for p in processes:
        p.join()

    # finalize
    # merge files
    merge_files(list_200_pre)
    merge_files(list_302_pre)
    merge_files(list_max_pre)
    merge_files(list_others_pre)
    merge_files(list_log_pre)

    elapsed_time = time.time() - start_time
    print '%.2fs, %.2f pages/min' % (elapsed_time, (end - start) / elapsed_time * 60)
        
if __name__ == "__main__":
    main()
