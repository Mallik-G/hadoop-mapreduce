#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    node_type = line[5]
    if node_type == "question":
        tags = line[2].split(" ")
        for tag in tags:
            if tag != "":
                writer.writerow([tag])
    else:
        continue
