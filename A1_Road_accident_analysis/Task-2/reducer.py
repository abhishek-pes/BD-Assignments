#!/usr/bin/env python3

import sys
current_state = None
current_city = None
current_der = None
current_count = 0
total_count = 0

for line in sys.stdin:
	try:
		line = line.strip()
		state,city = line.split(' ',1)
		count = 1
		flag = 1

		try:
			city = city.replace("%20"," ")
			city = city.replace("|","-")
			city = city.rstrip(city[-1])

		except:
			continue

		if(current_state != state):
			if(total_count != 0):
				flag = 0
				print(current_city.strip(),current_count)
				print(current_state.strip(),total_count)
				total_count = 0
			print(state.strip())
			
		if current_city == city:
			current_count += count
		else:
			if current_city and flag!=0:
				print(current_city.strip(),current_count)
			current_city = city
			current_count = count
			current_state = state
		total_count += 1
	except:
		continue
if current_city == city:
	print(current_city.strip(),current_count)
	if(total_count != 0):
		print(current_state.strip(),total_count)