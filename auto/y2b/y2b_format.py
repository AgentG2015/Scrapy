import os
import json
import natsort

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

json_dir = 'json'

def parse_conf():
    with open(os.path.join(bin_dir, '0.json'), 'r') as fd:
        return json.loads(fd.read())

def get_format(obj):
    return obj['url'], obj['audio']['format_id'], obj['video']['format_id']

def main():
    audio_set = set()
    video_set = set()
    for item in natsort.natsorted(os.listdir(json_dir)):
        with open(os.path.join(json_dir, item), 'r') as fd:
            obj = json.loads(fd.read())
            print obj['url'], obj['audio']['format_id'], obj['video']['format_id']
            audio_set.add(obj['audio']['format_id'])
            video_set.add(obj['video']['format_id'])
    print audio_set
    print video_set

if __name__ == '__main__':
    main()

