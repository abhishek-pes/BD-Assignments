#!/usr/bin/env python3

import sys

file_path = sys.argv[1]
f = open(file_path,'w')

def write_intial_page_index(page):
    f.write("%s,%s\n"%(page,1))

current_page = None
temp_l = []
for line in sys.stdin:
    line = line.strip()
    from_page,to_page = line.split(',',1)

    if current_page == from_page:
        temp_l.append(str(to_page))
    else:
        if current_page != None:
            print("%s$%s"%(int(current_page),temp_l))
            temp_l = []
            write_intial_page_index(int(current_page))
        current_page = from_page
        temp_l.append(str(to_page))


if current_page == from_page:
    print("%s$%s"%(int(current_page),temp_l))
    write_intial_page_index(int(current_page))
