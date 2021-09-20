#!/usr/bin/env python3

import sys
import math
import requests
import json
try:
	latitude = sys.argv[1]
	longitude = sys.argv[2]
	d = sys.argv[3]
except:
	arguments = sys.argv[1].split(" ")
	latitude = arguments[0]
	longitude = arguments[1]
	d = arguments[2]
def make_req(lat,lon):
	try:
		pload = {"latitude": lat,"longitude":lon}
		headers = {'Content-Type': 'application/json'}
		r = requests.post('http://20.185.44.219:5000/',json=pload)
		return r.text
		#res = json.loads(r.text)
		#print(res["state"].strip(),'|',res["city"].strip().replace(" ","%20"),'|',1);
		#print("%s\t%s"%(res["state"].strip(),res["city"].strip()))
	except:
		return

def euclid(lon1, lat1, lon2, lat2):
	try:
		ed = (math.sqrt((lon2 - lon1)**2 + (lat1 - lat2)**2))
		return ed
	except:
		return -1
    
for line in sys.stdin:
	line = line.strip()
	loaded = json.loads(line)
	try:
		#print(type(str(loaded['End_Lat'])))
		if(str(loaded['Start_Lat']) == "nan" or str(loaded['Start_Lng']) == "nan"):
			continue
		euclid_dist = euclid(float(loaded['Start_Lng']),float(loaded['Start_Lat']),float(longitude),float(latitude))
		if(euclid_dist <= float(d)):
			res = json.loads(make_req(float(loaded['Start_Lat']),float(loaded['Start_Lng'])))
			if(res['request-status'] == 'success' and res):
				if(res['state'] and ['city']):
					print("%s\t%s"%(res['state'],res['city']))
		else:
			continue
	except Exception as e:
		continue