#!/usr/bin/env python3

import sys

current_hour = None
current_count = 0
for line in sys.stdin:

	line = line.strip()
	hour,severity,ss = line.split('\t',2)
	count = 1

	if current_hour == hour:
		current_count += count
	else:
		if current_hour:
			print("%s\t%s"%(current_hour,current_count))
		current_hour = hour
		current_count = count
if current_hour == hour:
	print("%s\t%s"%(current_hour,current_count))

	#if int(severity) >= 2 and ss.lower() == "night":
