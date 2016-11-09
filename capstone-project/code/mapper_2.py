#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    node_type = line[5]
    if node_type == "question" or node_type == "answer":
        body = line[4]
        node_id = line[0]
        abs_parent_id = line[6]
        # if a question, there is no parent id and we want the node id
        # could also do if node_type == "question":
        if abs_parent_id == "\N":
            abs_id = node_id
        # if an answer, we want the parent id
        else:
            abs_id = abs_parent_id
        writer.writerow([abs_id, node_type, body])
    else:
        continue
