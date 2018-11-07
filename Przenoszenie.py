#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
import string
import math
import datetime
from shutil import copytree

a = os.listdir(sys.argv[1]) #sciezka do drzewa wejsciowego do Comps/

Comps = sys.argv[1]
CompsNeuro = sys.argv[2] #sciezka dla folderu neuronowego do WMNode

for folder in a:
	if folder == "bio" or folder == "config.conf" or folder == ".directory" or folder.endswith(".bin") or folder.endswith(".xml"):
		print folder
		continue
	brands = os.listdir(Comps+folder+"/ISNode/WMNode/")

	for l2folder in brands:
		l2change = l2folder
		if l2folder == "ScaleImages" or l2folder == ".directory" or l2folder == "config.conf" or l2folder == "config.conf~" or l2folder.endswith(".bin") or l2folder.endswith(".xml"):
			print folder+"/"+l2folder
			continue
		if l2folder == "360":
			l2change = ""
		l2brands360 = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder)

		for l3folder360 in l2brands360:
			if l3folder360 == "ScaleImages" or l3folder360 == "References" or l3folder360 == "config.conf" or l3folder360 == "config.conf~" or l3folder360 == ".directory" or l3folder360.endswith(".xml") or l3folder360.endswith(".bin"):
				print folder+"/"+l2folder+"/"+l3folder360
				continue
			if l3folder360 == "Patterns":
				Patterns = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/Patterns/")
				for UPIDY in Patterns:
					if UPIDY == ".directory" or UPIDY.endswith(".xml") == 1 or UPIDY.endswith(".bin") or UPIDY[0:5].isdigit() == 0:
						print UPIDY
						continue
					else:
						UPIDY = string.replace(UPIDY, '_0', '', 3)
						UPIDY = string.replace(UPIDY, '_1', '', 3)
						UPIDY = string.replace(UPIDY, '.bmp', '', 3)
						UPIDY = string.replace(UPIDY, '.png', '', 3)
						UPIDY = string.replace(UPIDY, '_mask', '', 3)
						copytree(Comps+folder+"/ISNode/WMNode/"+l2folder, CompsNeuro+UPIDY+"-"+folder+"-"+l2change)
						break
				break
			l3brands360 = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360)

			for l4folder360 in l3brands360:
				if l4folder360 == "ScaleImages" or l4folder360 == "References" or l4folder360 == "config.conf" or l4folder360 == "config.conf~" or l4folder360 == ".directory" or l4folder360.endswith(".xml") or l4folder360.endswith(".bin") == 1:
					print folder+"/"+l2folder+"/"+l3folder360+"/"+l4folder360
					continue
				if l4folder360 == "Patterns":
					Patterns = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/Patterns/")
					for UPIDY in Patterns:
						if UPIDY == ".directory" or UPIDY.endswith(".xml") == 1 or UPIDY.endswith(".bin") or UPIDY[0:5].isdigit() == 0:
							print UPIDY
							continue
						else:
							UPIDY = string.replace(UPIDY, '_0', '', 3)
							UPIDY = string.replace(UPIDY, '_1', '', 3)
							UPIDY = string.replace(UPIDY, '.bmp', '', 3)
							UPIDY = string.replace(UPIDY, '.png', '', 3)
							UPIDY = string.replace(UPIDY, '_mask', '', 3)
							copytree(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360, CompsNeuro+UPIDY+"-"+folder+"-"+l2change+"-"+l3folder360)
							break
					break
				l4brands360 = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360)

				for l5folder360 in l4brands360:
					if l5folder360 == "ScaleImages" or l5folder360=="References" or l5folder360 == "config.conf" or l5folder360 == "config.conf~" or l5folder360 == ".directory" or l5folder360.endswith(".xml") == 1 or l5folder360.endswith(".bin"):
						print folder+"/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360
						continue
					if l5folder360 == "Patterns":
						Patterns = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/Patterns/")
						for UPIDY in Patterns:
							if UPIDY == ".directory" or UPIDY.endswith(".xml") == 1 or UPIDY.endswith(".bin") or UPIDY[0:5].isdigit() == 0:
								print UPIDY
								continue
							else:
								UPIDY = string.replace(UPIDY, '_0', '', 3)
								UPIDY = string.replace(UPIDY, '_1', '', 3)
								UPIDY = string.replace(UPIDY, '.bmp', '', 3)
								UPIDY = string.replace(UPIDY, '.png', '', 3)
								UPIDY = string.replace(UPIDY, '_mask', '', 3)
								copytree(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360, CompsNeuro+UPIDY+"-"+folder+"-"+l2change+"-"+l3folder360+"-"+l4folder360)
								break
						break
					l5brands360 = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360)

					for l6folder360 in l5brands360:
						if l6folder360 == "ScaleImages" or l6folder360=="References" or l6folder360 == "config.conf" or l6folder360 == "config.conf~" or l6folder360 == ".directory" or l6folder360.endswith(".xml") == 1 or l6folder360.endswith(".bin"):
							print folder+"/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360+"/"+l6folder360
							continue
						if l6folder360 == "Patterns":
							Patterns = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360+"/Patterns/")
							for UPIDY in Patterns:
								if UPIDY == ".directory" or UPIDY.endswith(".xml") == 1 or UPIDY.endswith(".bin") or UPIDY[0:5].isdigit() == 0:
									print UPIDY
									continue
								else:
									UPIDY = string.replace(UPIDY, '_0', '', 3)
									UPIDY = string.replace(UPIDY, '_1', '', 3)
									UPIDY = string.replace(UPIDY, '.bmp', '', 3)
									UPIDY = string.replace(UPIDY, '.png', '', 3)
									UPIDY = string.replace(UPIDY, '_mask', '', 3)
									copytree(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360, CompsNeuro+UPIDY+"-"+folder+"-"+l2change+"-"+l3folder360+"-"+l4folder360+"-"+l5folder360)
									break
							break
						l6brands360 = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360+"/"+l6folder360)

						for l7folder360 in l6brands360:
							if l7folder360 == "ScaleImages" or l7folder360=="References" or l7folder360 == "config.conf" or l7folder360 == "config.conf~" or l7folder360 == ".directory" or l7folder360.endswith(".xml") == 1 or l7folder360.endswith(".bin"):
								print folder+"/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360+"/"+l6folder360+"/"+l7folder360
								continue
							if l7folder360 == "Patterns":
								Patterns = os.listdir(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360+"/"+l6folder360+"/Patterns/")
								for UPIDY in Patterns:
									if UPIDY == ".directory" or UPIDY.endswith(".xml") == 1 or UPIDY.endswith(".bin") or UPIDY[0:5].isdigit() == 0:
										print UPIDY
										continue
									else:
										UPIDY = string.replace(UPIDY, '_0', '', 3)
										UPIDY = string.replace(UPIDY, '_1', '', 3)
										UPIDY = string.replace(UPIDY, '.bmp', '', 3)
										UPIDY = string.replace(UPIDY, '.png', '', 3)
										UPIDY = string.replace(UPIDY, '_mask', '', 3)
										copytree(Comps+folder+"/ISNode/WMNode/"+l2folder+"/"+l3folder360+"/"+l4folder360+"/"+l5folder360+"/"+l6folder360, CompsNeuro+UPIDY+"-"+folder+"-"+l2change+"-"+l3folder360+"-"+l4folder360+"-"+l5folder360+"-"+l6folder360)
										break
								break

