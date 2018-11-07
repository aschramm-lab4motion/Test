#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import openpyxl
import random
import string
import math
import datetime
import time
from PIL import Image

conversion_route = "/home/l4m/l4m/bengurion-next/11-Conversion/"
conversion = os.listdir(conversion_route)

converted_route = "/home/l4m/l4m/bengurion-next/22-Converted/"
converted = os.listdir(converted_route)

source = "." + str(sys.argv[1])
source_small = source.lower()
source_big = source.upper()
output = "." + str(sys.argv[2])
output_small = output.lower()

date = datetime.date.today().strftime("%Y%m%d")
time = datetime.datetime.now().strftime("%H%M")
new_folder = date + "-" + time + "-" + sys.argv[2]

if os.path.isdir(converted_route + new_folder):
    os.mkdir(converted_route + new_folder + "n")
    save_path = converted_route + new_folder + "n/"
else:
    os.mkdir(converted_route + new_folder)
    save_path = converted_route + new_folder + "/"

for photo in conversion:
    photo2 = string.replace(photo, source_small, output_small, 1)
    photo2 = string.replace(photo2, source_big, output_small, 1)
    print photo2
    im = Image.open(conversion_route + photo)
    quality_val = 90
    im.save(save_path + photo2, quality=quality_val)
