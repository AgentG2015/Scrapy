import datetime
import time

with open('2.txt', 'r') as f1, open('3.txt', 'w') as f2:
    a_list = f1.read().strip().split('\n')[0::2]
    print a_list
    for a in a_list:
        f2.write(str(a.split('  ')[0]) + ', ')