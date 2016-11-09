#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    author_id = line[3]
    date_added = line[8]
    hour_added = date_added[11:13]
    if author_id == "author_id":
        continue
    else:
        writer.writerow([author_id, hour_added])

