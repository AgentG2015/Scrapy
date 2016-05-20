import os
import shutil

folder = 'bk/'

jpg_list = [f for f in os.listdir(folder) if os.path.splitext(f)[1] == '.jpg']
psd_list = [f for f in os.listdir(folder) if os.path.splitext(f)[1].lower() == '.psd']

print jpg_list
print psd_list
print len(jpg_list)
print len(psd_list)

for i, f in enumerate(jpg_list):
    src_name = folder + psd_list[i]
    dest_name = folder + os.path.splitext(f)[0] + os.path.splitext(src_name)[1]
    shutil.move(src_name, dest_name)
