import os
import shutil

for l in os.listdir():
    try:
        int(l)
        shutil.move(l, './Archives')
    except:
        pass
