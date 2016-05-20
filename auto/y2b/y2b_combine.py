import os
import json
import subprocess

combined_dir = 'combined'
download_dir = 'download'
json_dir = 'json'

def main():
    if not os.path.exists(combined_dir):
        os.makedirs(combined_dir)

    # load json_map
    json_map = {}
    filename_map = {}
    for json_file in os.listdir(json_dir):
        with open(os.path.join(json_dir, json_file), 'r') as fd:
            filename = json_file[:-5] + '.mp4'
            obj = json.loads(fd.read())
            json_map[obj['audio']['filesize']] = obj
            json_map[obj['video']['filesize']] = obj
            filename_map[obj['audio']['filesize']] = filename
            filename_map[obj['video']['filesize']] = filename

    # load down_map
    down_map = {}
    for item in os.listdir(download_dir):
        filesize = os.path.getsize(os.path.join(download_dir, item))
        down_map[filesize] = item

    # loop through download_dir
    looped_list = set()
    download_list = os.listdir(download_dir)
    remain_list = list(set(download_list) - looped_list)
    while len(remain_list) > 0:
        down_file = remain_list[0]
        filesize = os.path.getsize(os.path.join(download_dir, down_file))
        filename = filename_map[filesize]
        obj = json_map[filesize]
        try:
            # is audio file
            if filesize == obj['audio']['filesize']:
                video_filesize = obj['video']['filesize']
                audio_file = down_map[filesize]
                video_file = down_map[video_filesize]
            else:
                audio_filesize = obj['audio']['filesize']
                audio_file = down_map[audio_filesize]
                video_file = down_map[filesize]
        except KeyError:
            looped_list.add(down_file)
            remain_list = list(set(download_list) - looped_list)
            continue
        cmd = 'ffmpeg -y -i "%s" -i "%s" -map 0 -map 1 -acodec copy -vcodec copy -shortest "%s"' \
              % ( os.path.join(download_dir, audio_file),
                  os.path.join(download_dir, video_file),
                  os.path.join(combined_dir, filename))
        print cmd
        subprocess.call(cmd, shell=True)
        os.remove(os.path.join(download_dir, audio_file))
        os.remove(os.path.join(download_dir, video_file))
        looped_list.add(audio_file)
        looped_list.add(video_file)
        download_list = os.listdir(download_dir)
        remain_list = list(set(download_list) - looped_list)

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        raw_input()