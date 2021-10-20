#!/usr/bin/env python3

import sys
import json
import math

path_to_v = sys.argv[1]
embedding_file = sys.argv[2]


f1 = open(embedding_file)
data = json.load(f1)

f2 = open(path_to_v,'r')

v_dict = dict()
for lines in f2.readlines():
    v_dict[lines.split(',')[0]] = lines.split(',')[1].rstrip('\t\n')
#print(v_dict)


# function to calculate cosine similarity
def cosine_similarity(node,adjacency_list):
    initial_contribution = float(v_dict[str(node)])/len(adjacency_list)
    print("%s,%s,%s"%(node,node,0))
    for links in adjacency_list:
        links = links.strip("'")
        v1 = data[str(node)]
        v2 = data[links]
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i]; y = v2[i]
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
        print("%s,%s,%s"%(links,node,initial_contribution*(sumxy/math.sqrt(sumxx*sumyy))))



for line in sys.stdin:
    line = line.strip()
    from_node = line.split('$')[0]
    adjacency_list = line.split('$')[1]
    adjacency_list = adjacency_list.strip('][').split(', ')
    cosine_similarity(from_node,adjacency_list)