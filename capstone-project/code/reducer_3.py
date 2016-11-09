#!/usr/bin/python

import sys

oldTag = None
tagCount = 0
top10 = {}

# loop through tags (auto-sorted via hadoop)
# when tag changes:
# dictionary of size 10 with tag as key, tag count as value
# fill up first 10
# see if tag count > 10th, if so, pop and sort
# after last line, print top 10 tags

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisTag =  data_mapped[0]
    
    # new tag so check with dictionary of tag counts
    if oldTag and oldTag != thisTag:
        if len(top10) < 10:
            top10[oldTag] = tagCount
        elif tagCount > min(top10.itervalues()):
            delKey = min(top10, key=top10.get)
            del top10[delKey]
            top10[oldTag] = tagCount
        # reset tag count
        oldTag = thisTag
        tagCount = 0

    tagCount += 1
    oldTag = thisTag

# check last line
if oldTag != None:
   if len(top10) < 10:
       top10[oldTag] = tagCount
   elif tagCount > min(top10.itervalues()):
       delKey = min(top10, key=top10.get)
       del top10[delKey]
       top10[oldTag] = tagCount

print sorted(((v,k) for k,v in top10.iteritems()), reverse=True)
