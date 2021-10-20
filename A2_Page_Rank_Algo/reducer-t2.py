#!/usr/bin/env python3

import sys

current_page = None
contribution_sum = 0
for line in sys.stdin:
    line = line.strip()
    from_page,to_page,c_score = line.split(',',2)
    if current_page == from_page:
        contribution_sum = contribution_sum + float(c_score)
    else:
        if current_page != None:
            print("%s,%.2f"%(int(current_page),0.15 + 0.85*contribution_sum))
            contribution_sum = 0
        current_page = from_page
        contribution_sum = contribution_sum + float(c_score)


if current_page == from_page:
    print("%s,%.2f"%(int(current_page),0.15 + 0.85*contribution_sum))
