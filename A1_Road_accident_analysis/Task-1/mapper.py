#!/usr/bin/env python3

import sys
import json
from datetime import datetime

#cat test.json | python3 mapper.py | sort -n -s -k1,1 | python3 reducer.py

def check_wc(val):

	try:
		if val.lower() in ['heavy snow','thunderstorm','heavy rain','heavy rain showers','blowing dust']:
			return True
	except:
		return False
def check_desc(val):

	try:
		if 'lane blocked' in val.lower() or 'shoulder blocked' in val.lower() or 'overturned vehicle' in val.lower():
			#print(val.lower())
			return True
	except:
		return False

for line in sys.stdin:
	line = line.strip()
	loaded = json.loads(line)
	try:
		if  float(loaded['Severity'])>=2 and loaded['Sunrise_Sunset'].lower() == "night" and float(loaded['Visibility(mi)']) <= 10 and float(loaded['Precipitation(in)']) >= 0.2 and check_desc(loaded['Description']) and check_wc(loaded['Weather_Condition']):
			try:
				dt_obj = datetime.strptime(loaded["Start_Time"],'%Y-%m-%d %H:%M:%S')
				print("%s\t%s\t%s"%(str(dt_obj.hour).zfill(2),loaded["Severity"],loaded["Sunrise_Sunset"]))
		
			except Exception as e:
				temp_time = loaded["Start_Time"].rstrip('0')
				#print(temp_time)
				dt_obj = datetime.strptime(temp_time,'%Y-%m-%d %H:%M:%S.')
				#print(e)
				print("%s\t%s\t%s"%(str(dt_obj.hour).zfill(2),loaded["Severity"],loaded["Sunrise_Sunset"]))
		else:
			continue
	except:
		continue