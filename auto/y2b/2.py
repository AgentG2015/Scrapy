import os
import re
import json

import natsort
import chardet
from youtube_dl.utils import sanitize_filename

json_dir = 'json'

def main():
    info_list = get_info_list()
    download_set = set([src_name[:-4] for src_name in os.listdir('.') if not src_name.endswith('.py') and not os.path.isdir(src_name)])

    count = 0
    for info in filter(lambda x: x.title not in download_set, info_list):
        count += 1
        print_error_info(info)
    raw_input('%s miss' % count)

def print_error_info(info):
    print (info.i, info.title, info.sanitized_filename, info.json_obj['url'], info.json_obj['audio']['format_id'], info.json_obj['video']['format_id'])

def get_info_list():
    info_list = []
    for i, item in enumerate(natsort.natsorted(os.listdir(json_dir))):
        title = item[:-5]
        filepath = os.path.join(json_dir, item)
        info = DownloadInfo(i + 1, title, filepath)
        info_list.append(info)
    return info_list

class DownloadInfo:
    cmd_tpl = 'ytd %s %s %s'

    def __init__(self, i, title, filepath):
        self.i = i
        self.title = title
        self.filepath = filepath
        with open(filepath, 'r') as fd:
            self.json_obj = json.loads(fd.read())
        self.sanitized_filename = sanitize_filename(self.json_obj['original_title'], restricted=True)
        self.cmd = DownloadInfo.cmd_tpl % (self.json_obj['url'], self.json_obj['audio']['format_id'], self.json_obj['video']['format_id'])

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        raw_input()