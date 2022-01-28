#!/usr/bin/env python3

from PIL import Image
import os

imgdirname = os.path.expanduser('~') + '/images/'
newimagelocation = '/opt/icons/'

for dirpath, dirnames, filenames in os.walk(imgdirname):

    for file in filenames:
        if not file.endswith(('.DS_Store')):
            newfilename = os.path.join(newimagelocation, file)
            im = Image.open(os.path.join(dirpath, file))
            im.resize((128,128)).convert('RGB').rotate(-90).save(newfilename, "JPEG")

print("done!")
