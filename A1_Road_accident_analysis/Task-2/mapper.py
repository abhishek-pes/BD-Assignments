#!/usr/bin/env python3

import sys
from math import radians, cos, sin, asin, sqrt
import requests
import json
latitude = sys.argv[1]
longitude = sys.argv[2]
d = sys.argv[3]

def make_req(lat,lon):
	try:
		pload = {"latitude": lat,"longitude":lon}
		headers = {'Content-Type': 'application/json'}
		r = requests.post('http://20.185.44.219:5000/',json=pload)
		#print(r.text)
		res = json.loads(r.text)
		print(res["state"].strip(),'|',res["city"].strip().replace(" ","%20"),'|',1);
		#print("%s\t%s\t%s"%(res["state"].strip(),res["city"].strip(),1))
	except:
		return

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """

    # convert decimal degrees to radians 
    #lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    #print(dlon,dlat)
    ed = (sqrt((lon2 - lon1)**2 + (lat1 - lat2)**2))
    return ed
    #a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    #c = 2 * asin(sqrt(a)) 
    #print(c)
    # Radius of earth in kilometers is 6371
    # km = 6371* c
    #return km
    
for line in sys.stdin:
	line = line.strip()
	loaded = json.loads(line)
	try:
		euclid_dist = haversine(float(loaded['Start_Lng']),float(loaded['Start_Lat']),float(longitude),float(latitude))
		if(euclid_dist <= float(d)):
			make_req(float(loaded['Start_Lat']),float(loaded['Start_Lng']))
			#print('The distance is ',euclid_dist)
		else:
			continue
	except:
		continue