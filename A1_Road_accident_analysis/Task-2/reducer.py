#!/usr/bin/env python3

import sys
current_state = None
current_city = None
current_count = 0
total_count = 0

for line in sys.stdin:

	line = line.strip()
	#print(line.split('|'),2)
	#print(line.split('|'))
	#state = line.split('|').strip()
	#print(state)
	#state,city,count = line.split('|',2)
	#print(state,city,count)
	state,city,count = line.split('|',2)
	count = int(count)
	flag = 1
	try:
		city = city.replace("%20"," ")
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
			#print("%s\t%s"%(current_city,current_count))
		current_city = city
		current_count = count
		current_state = state
	total_count += 1
if current_city == city:
	print(current_city.strip(),current_count)
	if(total_count != 0):
		print(current_state.strip(),total_count)
	#print("%s\t%s"%(current_city,current_count))