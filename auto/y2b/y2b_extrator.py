from __future__ import unicode_literals

import json
import youtube_dl

"""
Video Format:
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

url = 'https://www.youtube.com/watch?v=2ZoTIseY8yo'

def pretty_json(obj):
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))

def main():
    ydl = youtube_dl.YoutubeDL()
    with ydl:
        result = ydl.extract_info(url, download=False)
        with open('1.txt', 'w') as fd:
            fd.write(pretty_json(result))

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        raw_input()
