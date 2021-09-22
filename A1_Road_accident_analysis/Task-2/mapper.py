#!/usr/bin/env python3

import sys
import math
import requests
import json
try:
	latitude = float(sys.argv[1])
	longitude = float(sys.argv[2])
	d = float(sys.argv[3])
except:
	arguments = sys.argv[1].split(" ")
	latitude = float(arguments[0])
	longitude = float(arguments[1])
	d = float(arguments[2])

def make_req(lat,lon):	
	pload = {"latitude": lat,"longitude":lon }
	r = requests.post('http://20.185.44.219:5000/',json=pload)
	return r.json()

count = 0
latarr = []
lonarr = []    
for line in sys.stdin:
	line = line.strip()
	loaded = json.loads(line)
	try:
		lat = float(loaded['Start_Lat'])
		long = float(loaded['Start_Lng'])
		if (math.sqrt((long - longitude)**2 + (lat - latitude)**2)) <= d:
			res = make_req(lat,long)
			try:
				city = res["city"].split(" ")
				print(res["state"],city[0]+"%20"+city[1].replace("-","|")+"z")
			except:
				print(res["state"],res["city"].replace("-","|")+"z")
	except Exception as e:
		continue