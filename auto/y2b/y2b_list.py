from __future__ import unicode_literals

from gevent import monkey
monkey.patch_all()

import os
import re
import json
import requests
import youtube_dl
import natsort
from lxml import html
from gevent.pool import Pool

"""
Video Format:
299: 1080p 60fps
298: 1080p 60fps
266: 2160p
264: 1440p
138: 1440p
137: 1080p
136: 720p
135: 480p
134: 360p
133: 240p
Audio Format:
140: 128k
141: 256k
"""

y2b_root_url = 'https://www.youtube.com'
video_exclude_format_list = [299, 298, 266, 264, 138]
video_format_list = [137, 136, 135, 134, 133]
audio_format_list = [141, 140]
pool_size = 50
max_retry_count = 10
json_dir = 'json'
invalid_escape = re.compile(r'\\[0-7]{1,3}')  # up to 3 digits for byte values up to FF

def replace_with_byte(match):
    return chr(int(match.group(0)[1:], 8))

def repair(brokenjson):
    return invalid_escape.sub(replace_with_byte, brokenjson)

def int_or_0(raw_string):
    if raw_string.isdigit():
        return int(raw_string)
    else:
        return 0

def to_clean_filename(raw_string):
    return re.sub(r'[/\\:*?"<>|]', '', raw_string)

def pretty_json(obj):
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))

def get_entry_tuple(result):
    max_video_filesize = 0
    max_audio_format = 0
    max_video = {}
    max_audio = {}
    format_list = result['formats']
    for item in format_list:
        format_id = int_or_0(item['format_id'])
        if format_id == 0:
            continue
        if format_id in video_exclude_format_list:
            continue
        if format_id in audio_format_list:
            if format_id > max_audio_format:
                max_audio_format = format_id
                max_audio = item
        else:
            if 'DASH' in item['format'] and 'filesize' in item and 'ext' in item and item['ext'] == 'mp4' and item['filesize'] > max_video_filesize:
                max_video_filesize = item['filesize']
                max_video = item

    return max_video, max_audio

def parse_conf():
    with open('0.json', 'r') as fd:
        return json.loads(fd.read())

def get_rid_suffix(url):
    return url[:url.find("&")]

def get_url_list_xpath(content_html):
    tree = html.fromstring(content_html)
    nodes = tree.xpath('//a[@class="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "]/@href')
    return [y2b_root_url + get_rid_suffix(node.strip()) for node in nodes]

def get_url_list_regex(content_html, list_id):
    reg = re.compile(r'/watch\?v=\S+?list=' + list_id)
    match_list = re.findall(reg, content_html)
    temp_dict = OrderedDict()
    for item in match_list:
        temp_dict[y2b_root_url + get_rid_suffix(item)] = item
    return list(temp_dict)

def get_url_list(list_url):
    """
    get url list if not exists
    """
    filename = 'list.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as fd:
            return fd.read().split('\n')
    else:
        r = requests.get(list_url)
        content_html = r.text
        ret = get_url_list_xpath(content_html)
        tree = html.fromstring(content_html)
        nodes = tree.xpath('//button[@class="yt-uix-button yt-uix-button-size-default yt-uix-button-default load-more-button yt-uix-load-more browse-items-load-more-button"]/@data-uix-load-more-href')
        if len(nodes) > 0:
            load_more_url = y2b_root_url + nodes[0]
            print load_more_url
            r = requests.get(load_more_url)
            content_html = json.loads(r.text)['content_html']
            ret.extend(get_url_list_xpath(content_html))

        # write to local file
        with open(filename, 'w') as fd:
            end = len(ret)
            for i, line in enumerate(ret):
                if i == end - 1:
                    fd.write(line)
                else:
                    fd.write(line + '\n')
        return ret

def worker(url):
    tried_count = 0
    while tried_count < max_retry_count:
        try:
            ydl = youtube_dl.YoutubeDL()
            with ydl:
                result = ydl.extract_info(url, download=False)

            title = to_clean_filename(result['title'])
            original_title = result['title']
            filename = title + '.json'

            max_video, max_audio = get_entry_tuple(result)
            obj = {'url': url,
                   'original_title': original_title,
                   'video': {'format_id': max_video['format_id'], 'filesize': max_video['filesize'], 'url': max_video['url']},
                   'audio': {'format_id': max_audio['format_id'], 'filesize': max_audio['filesize'], 'url': max_audio['url']}}

            with open(os.path.join(json_dir, filename), 'w') as fd:
                fd.write(pretty_json(obj))
            break
        except:
            tried_count += 1
    else:
        print "momomomo: %s" % url

def gen_downlist():
    with open('1.downlist', 'w') as fd:
        for item in natsort.natsorted(os.listdir(json_dir)):
            with open(os.path.join(json_dir, item), 'r') as json_file:
                obj = json.loads(json_file.read())
                fd.write(obj['audio']['url'] + '\n')
                fd.write(obj['video']['url'] + '\n')

def gen_misslist(url_list):
    misslist_filename = 'miss.txt'
    # remove first
    if os.path.exists(misslist_filename):
        os.remove(misslist_filename)

    # base_url_set
    base_url_set = set(url_list)

    # json_map
    json_map = {}
    for item in os.listdir(json_dir):
        with open(os.path.join(json_dir, item), 'r') as fd:
            obj = json.loads(fd.read())
            json_map[obj['url']] = obj

    # miss_list
    miss_list = []
    for item in base_url_set:
        if not item in json_map:
            miss_list.append(item)

    # gen file
    if len(miss_list) > 0:
        with open(misslist_filename, 'w') as fd:
            for item in miss_list:
                fd.write(item + '\n')

def main():
    conf = parse_conf()
    list_url = conf['list_url']

    url_list = get_url_list(list_url)

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    pool = Pool(pool_size)
    sep_list = conf['sep_list']

    if len(sep_list) > 0:
        for i in sep_list:
            pool.spawn(worker, url_list[i - 1])
        pool.join()
    else:
        start = conf['start'] - 1
        end = conf['end']
        if end == 0:
            end = len(url_list)

        for i in range(start, end):
            pool.spawn(worker, url_list[i])
        pool.join()

    # generate Thunder downlist
    gen_downlist()
    gen_misslist(url_list)

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        raw_input()
