# -*- coding=UTF-8 -*-

import shutil
import os

folder = u'CG游麟网43.5G-CGTextures-V06/Ornaments'

try:
    f_list = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
    for f in f_list:
        print f
        rindex = f.rfind('-')
        if rindex > 0:
            src = os.path.join(folder, f)
            dest = os.path.join(folder, f[:rindex].strip().title())
            shutil.move(src, dest)
except Exception as e:
    raw_input('Exception: ' + str(e))