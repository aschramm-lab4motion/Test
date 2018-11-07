#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
import string
import math
import datetime
import random
from shutil import copytree
from shutil import copyfile

# Opcje skryptu:
# (nazwa) sciezka_do_folderu

Copy = sys.argv[1]
From = "/home/l4m/l4m/bengurion-next/Tworzenie_drzewa_Mondelez/"
Copy_list = os.listdir(Copy)
n=0
m=0
o=0

for folder in Copy_list:
	copytree(From+"ISNode", Copy+"logo-"+folder[:len(folder)-10]+"/ISNode")
	copyfile(From+"config.conf", Copy+"logo-"+folder[:len(folder)-10]+"/config.conf")
	copyfile(Copy+folder, Copy+"logo-"+folder[:len(folder)-10]+"/ISNode/WMNode/NBlack/Patterns/"+folder)
	os.rename(Copy+"logo-"+folder[:len(folder)-10]+"/ISNode/WMNode/NBlack", Copy+"logo-"+folder[:len(folder)-10]+"/ISNode/WMNode/"+folder[:len(folder)-10])
	print folder
	with open(Copy+"logo-"+folder[:len(folder)-10]+"/ISNode/WMNode/"+folder[:len(folder)-10]+"/config.conf",'r+') as file:
		lines = file.readlines()
		file.seek(0)
		file.truncate()
		for line in lines:
			if "UPID:" in line:
				line = "UPID:                "+folder[:len(folder)-6]+"\n"
			if "wholeBottle:" in line:
				line = "wholeBottle:         10\n"
			if "size{}" in line:
				line = "size\n{\n  10\n  10\n}\n"
			if "color{}" in line:
				n = random.randint(1, 254)
				nn = str(n)
				m = random.randint(1, 254)
				mm = str(m)
				o = random.randint(1, 254)
				oo = str(o)
				line = "color\n{\n  "+nn+"\n  "+mm+"\n  "+oo+"\n}\n"
			file.write(line)
