import os
import json

def main():
    # base_url_set
    filename = 'list.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as fd:
            base_url_set = set(fd.read().split('\n'))

    # json_map
    json_map = {}
    for item in os.listdir('json'):
        with open(os.path.join('json', item), 'r') as fd:
            obj = json.loads(fd.read())
            json_map[obj['url']] = obj

    # miss_list
    miss_list = []
    for item in base_url_set:
        if not item in json_map:
            miss_list.append(item)

    print len(miss_list)

if __name__ == '__main__':
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        raw_input()
