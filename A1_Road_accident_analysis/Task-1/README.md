code to run task 1 : ```cat US_ACCIDENT_DATA_5PERCENT.json | python3 mapper.py | sort -n -s -k1,1 | python3 reducer.py```