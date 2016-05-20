import os
import re
import json
import natsort
import chardet

json_dir = 'json'

def main():
    info_list = get_info_list()

    renamed_count = 0
    for src_name in os.listdir('.'):
        if src_name in __file__ or os.path.isdir(src_name):
            continue
        encoding = chardet.detect(src_name)['encoding']
        decoded_src_name = src_name.decode(encoding)
        renamed = False
        for info in info_list:
            if src_name[:-4] == info.title:
                renamed = True
                break
            if decoded_src_name[:-4].startswith(info.sanitized_filename):
                dest_name = info.title + '.mp4'
                os.rename(src_name, dest_name)
                renamed_count += 1
                renamed = True
                break
        if not renamed:
            print decoded_src_name.encode(encoding)

    raw_input('%s renamed' % renamed_count)

def get_info_list():
    info_list = []
    for i, item in enumerate(natsort.natsorted(os.listdir(json_dir))):
        title = item[:-5]
        filepath = os.path.join(json_dir, item)
        info = DownloadInfo(i + 1, title, filepath)
        info_list.append(info)
    return info_list

def sanitize_filename(s, restricted=False, is_id=False):
    """Sanitizes a string so it could be used as part of a filename.
    If restricted is set, use a stricter subset of allowed characters.
    Set is_id if this is not an arbitrary string, but an ID that should be kept if possible
    """
    def replace_insane(char):
        if char == '?' or ord(char) < 32 or ord(char) == 127:
            return ''
        elif char == '"':
            return '' if restricted else '\''
        elif char == ':':
            return '_-' if restricted else ' -'
        elif char in '\\/|*<>':
            return '_'
        if restricted and (char in '!&\'()[]{}$;`^,#' or char.isspace()):
            return '_'
        if restricted and ord(char) > 127:
            return '_'
        return char

    # Handle timestamps
    s = re.sub(r'[0-9]+(?::[0-9]+)+', lambda m: m.group(0).replace(':', '_'), s)
    result = ''.join(map(replace_insane, s))
    if not is_id:
        while '__' in result:
            result = result.replace('__', '_')
        result = result.strip('_')
        # Common case of "Foreign band name - English song title"
        if restricted and result.startswith('-_'):
            result = result[2:]
        if result.startswith('-'):
            result = '_' + result[len('-'):]
        result = result.lstrip('.')
        if not result:
            result = '_'
    return result

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