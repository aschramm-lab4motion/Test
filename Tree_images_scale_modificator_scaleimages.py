#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
import string
# import math
# import datetime
# from os.path import join, getsize, isdir
from os.path import isdir
from shutil import copytree
from shutil import rmtree
# import time
# import argparse
from subprocess import check_output
from PIL import Image

# parser = argparse.ArgumentParser(description='Extract products from classic \
# tree to neuron folder based on list.txt Syntax: [script_name] [tree_path_to_\
# Comps] [neuron_folder_name]')
# parser.add_argument('integers', metavar='N', type=str, nargs='+',
# help='an integer for the accumulator')
# parser.add_argument('integers', metavar='N', type=str, nargs='+',
# help='an integer for the accumulator')
# args = parser.parse_args()


def Is_Patterns_Initial(Path, Folder):
    Result = True
    if isdir(Path + Folder) is False:
        Result = False
    if Folder == "bio" or Folder == ".directory":
        Result = False
    return(Result)


def Is_Patterns(Path, Folder):
    Result = True
    if isdir(Path + "/" + Folder) is False:
        Result = False
    if Folder == ".directory":
        Result = False
    return(Result)


def Is_UPID(UPID):
    Result = True
    if UPID == ".directory" or UPID.endswith((".xml", ".bin")) == 1:
        Result = False
    if UPID[0:5].isdigit() == 0:
        Result = False
    if UPID.endswith(".png") == 0:
        Result = False
    return(Result)

def Is_Scale(UPID):
    Result = True
    if UPID == ".directory" or UPID.endswith((".xml", ".bin")) == 1:
        Result = False
    if UPID.endswith(".png") == 0 and UPID.endswith(".bmp") == 0:
        Result = False
    return(Result)


path_check = sys.argv[1]

if path_check[len(path_check) - 1:len(path_check)] != "/":
    path_check = path_check + "/"

if path_check[len(path_check) - 7:len(path_check)] != "/Comps/":
    print "Path must end on /Comps/"
    sys.exit(0)

Main = os.listdir(path_check)  # sciezka do drzewa wejsciowego do Comps/

Comps = path_check

NPT = ""
quality_val = 90
scal = 2
counter = 0

# Done_tab = list(range(0,101))
# Progress_tab = list(range(0,101))
# Done_tab[0] = ""
# Progress_tab[0] = ""
# Spaces = ""
# y = 0
# prog_counter = 1
# while prog_counter <= 100:
# paces = ""
# y = 0
# Done_tab[prog_counter] = Done_tab[prog_counter-1]+"*"
# rewq = 100 - prog_counter
# while y < rewq:
# paces = Spaces+" "
# y = y+1
# print "start:"+Spaces+":end"
# Progress_tab[prog_counter] = "["+Done_tab[prog_counter]+Spaces+"]"
# prog_counter = prog_counter + 1
# copytree(Neural_path_short, Comps+"Neural")

UPI_counter = 0

# time.sleep(1000)
All_UP = list(range(0, UPI_counter))
UPI_counter_new = 0

for folder in Main:
    if Is_Patterns_Initial(Comps, folder) is False:
        continue
    new_path = os.path.join(Comps + folder, "ISNode/WMNode/")
    brands = os.listdir(new_path)

    for l2folder in brands:
        l2change = l2folder
        if Is_Patterns(new_path, l2folder) is False:
            continue
        if l2folder == "360":
            l2change = ""
        P2 = os.path.join(new_path, l2folder)
        #  print NPN
        l2brands360 = os.listdir(P2)

        for l3folder360 in l2brands360:
            if Is_Patterns(P2, l3folder360) is False:
                continue
            if l3folder360 == "Scale":
                Scales = os.listdir(P2 + "/Scale/")
                for UPIDY_scale in Scales:
                    if Is_Scale(UPIDY_scale) is True:
                        im = Image.open(P2 + "/Scale/" + UPIDY_scale)
                        width, height = im.size
                        im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                        im.save(P2 + "/Scale/" + UPIDY_scale, quality = quality_val)
                        print P2 + "/Scale/" + UPIDY_scale + " was successfully scaled!"
                        counter = counter + 1
                    else:
                        continue
            if l3folder360 == "Patterns":
                Patterns = os.listdir(P2 + "/Patterns/")
                for UPIDY in Patterns:
                    if Is_UPID(UPIDY) is True:
                        im = Image.open(P2 + "/Patterns/" + UPIDY)
                        width, height = im.size
                        im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                        im.save(P2 + "/Patterns/" + UPIDY, quality = quality_val)
                        print P2 + "/Patterns/" + UPIDY + " was successfully scaled!"
                        counter = counter + 1
                    else:
                        continue
                break

            P3 = os.path.join(P2, l3folder360)
            l3brands360 = os.listdir(P3)

            for l4folder360 in l3brands360:
                if Is_Patterns(P3, l4folder360) is False:
                    continue
                if l4folder360 == "Scale":
                    Scales = os.listdir(P3 + "/Scale/")
                    for UPIDY_scale in Scales:
                        if Is_Scale(UPIDY_scale) is True:
                            im = Image.open(P3 + "/Scale/" + UPIDY_scale)
                            width, height = im.size
                            im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                            im.save(P3 + "/Scale/" + UPIDY_scale, quality = quality_val)
                            print P3 + "/Scale/" + UPIDY_scale + " was successfully scaled!"
                            counter = counter + 1
                        else:
                            continue
                if l4folder360 == "Patterns":
                    Patterns = os.listdir(P3 + "/Patterns/")
                    for UPIDY in Patterns:
                        if Is_UPID(UPIDY) is True:
                            im = Image.open(P3 + "/Patterns/" + UPIDY)
                            width, height = im.size
                            im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                            im.save(P3 + "/Patterns/" + UPIDY, quality = quality_val)
                            print P3 + "/Patterns/" + UPIDY + " was successfully scaled!"
                            counter = counter + 1
                        else:
                            continue
                    break

                P4 = os.path.join(P3, l4folder360)
                l4brands360 = os.listdir(P4)

                for l5folder360 in l4brands360:
                    if Is_Patterns(P4, l5folder360) is False:
                        continue
                    if l5folder360 == "Scale":
                        Scales = os.listdir(P4 + "/Scale/")
                        for UPIDY_scale in Scales:
                            if Is_Scale(UPIDY_scale) is True:
                                im = Image.open(P4 + "/Scale/" + UPIDY_scale)
                                width, height = im.size
                                im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                im.save(P4 + "/Scale/" + UPIDY_scale, quality = quality_val)
                                print P4 + "/Scale/" + UPIDY_scale + " was successfully scaled!"
                                counter = counter + 1
                            else:
                                continue
                    if l5folder360 == "Patterns":
                        Patterns = os.listdir(P4 + "/Patterns/")
                        for UPIDY in Patterns:
                            if Is_UPID(UPIDY) is True:
                                im = Image.open(P4 + "/Patterns/" + UPIDY)
                                width, height = im.size
                                im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                im.save(P4 + "/Patterns/" + UPIDY, quality = quality_val)
                                print P4 + "/Patterns/" + UPIDY + " was successfully scaled!"
                                counter = counter + 1
                            else:
                                continue
                        break

                    P5 = os.path.join(P4, l5folder360)
                    l5brands360 = os.listdir(P5)

                    for l6folder360 in l5brands360:
                        if Is_Patterns(P5, l6folder360) is False:
                            continue
                        if l6folder360 == "Scale":
                            Scales = os.listdir(P5 + "/Scale/")
                            for UPIDY_scale in Scales:
                                if Is_Scale(UPIDY_scale) is True:
                                    im = Image.open(P5 + "/Scale/" + UPIDY_scale)
                                    width, height = im.size
                                    im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                    im.save(P5 + "/Scale/" + UPIDY_scale, quality = quality_val)
                                    print P5 + "/Scale/" + UPIDY_scale + " was successfully scaled!"
                                    counter = counter + 1
                                else:
                                    continue
                        if l6folder360 == "Patterns":
                            Patterns = os.listdir(P5 + "/Patterns/")
                            for UPIDY in Patterns:
                                if Is_UPID(UPIDY) is True:
                                    im = Image.open(P5 + "/Patterns/" + UPIDY)
                                    width, height = im.size
                                    im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                    im.save(P5 + "/Patterns/" + UPIDY, quality = quality_val)
                                    print P5 + "/Patterns/" + UPIDY + " was successfully scaled!"
                                    counter = counter + 1
                                else:
                                    continue
                            break

                        P6 = os.path.join(P5, l6folder360)
                        l6brands360 = os.listdir(P6)

                        for l7folder360 in l6brands360:
                            if Is_Patterns(P6, l7folder360) is False:
                                continue
                            if l7folder360 == "Scale":
                                Scales = os.listdir(P6 + "/Scale/")
                                for UPIDY_scale in Scales:
                                    if Is_Scale(UPIDY_scale) is True:
                                        im = Image.open(P6 + "/Scale/" + UPIDY_scale)
                                        width, height = im.size
                                        im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                        im.save(P6 + "/Scale/" + UPIDY_scale, quality = quality_val)
                                        print P6 + "/Scale/" + UPIDY_scale + " was successfully scaled!"
                                        counter = counter + 1
                                    else:
                                        continue
                            if l7folder360 == "Patterns":
                                Patterns = os.listdir(P6 + "/Patterns/")
                                for UPIDY in Patterns:
                                    if Is_UPID(UPIDY) is True:
                                        im = Image.open(P6 + "/Patterns/" + UPIDY)
                                        width, height = im.size
                                        im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                        im.save(P6 + "/Patterns/" + UPIDY, quality = quality_val)
                                        print P6 + "/Patterns/" + UPIDY + " was successfully scaled!"
                                        counter = counter + 1
                                    else:
                                        continue

                                break

                            P7 = os.path.join(P6, l7folder360)
                            l7brands360 = os.listdir(P7)

                            for l8folder360 in l7brands360:
                                if Is_Patterns(P7, l8folder360) is False:
                                    continue
                                if l8folder360 == "Scale":
                                    Scales = os.listdir(P7 + "/Scale/")
                                    for UPIDY_scale in Scales:
                                        if Is_Scale(UPIDY_scale) is True:
                                            im = Image.open(P7 + "/Scale/" + UPIDY_scale)
                                            width, height = im.size
                                            im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                            im.save(P7 + "/Scale/" + UPIDY_scale, quality = quality_val)
                                            print P7 + "/Scale/" + UPIDY_scale + " was successfully scaled!"
                                            counter = counter + 1
                                        else:
                                            continue
                                if l8folder360 == "Patterns":
                                    Patterns = os.listdir(P7 + "/Patterns/")
                                    for UPIDY in Patterns:
                                        if Is_UPID(UPIDY) is True:
                                            im = Image.open(P7 + "/Patterns/" + UPIDY)
                                            width, height = im.size
                                            im = im.resize((width / 3 * scal, height / 3 * scal), Image.ANTIALIAS)
                                            im.save(P7 + "/Patterns/" + UPIDY, quality = quality_val)
                                            print P7 + "/Patterns/" + UPIDY + " was successfully scaled!"
                                            counter = counter + 1
                                        else:
                                            continue
                                    break

print "\nSuccessfully scaled images: " + str(counter) + "\n"
