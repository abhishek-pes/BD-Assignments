#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    from_page = line.split('\t')[0]
    to_page = line.split('\t')[1]
    print("%s,%s"%(from_page,to_page))
