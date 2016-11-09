#!/usr/bin/python

import sys

oldAbsID = None
lengthOrig = None
sumLength = 0
countAnswers = 0

# loop through ids (auto-sorted via hadoop)
# store length of post
# sum length of answers, number of answers
# when parent id changes, calculate average answer and print it along side post length

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    thisAbsID, thisNodeType, thisBody =  data_mapped
    
    # new id so it is time to print the old Q length
    # and average A length
    if oldAbsID and oldAbsID != thisAbsID:
        if countAnswers != 0:
            print lengthOrig, "\t", float(sumLength / countAnswers)
        else:
            print lengthOrig, "\t", 0
        # reset the user and the list of hours that user posted
        oldAbsID = thisAbsID
        lengthOrig = None
        sumLength = 0
        countAnswers = 0

    oldAbsID = thisAbsID
    # will catch question eventually via looping through sorted ids
    if thisNodeType[1:-1] == "question":
        lengthOrig = len(thisBody)
    # add too sum of answer length and answer count
    else:
        sumLength += len(thisBody)
        countAnswers += 1

# print the last line so print the old Q length and average A length
if oldAbsID != None:
    if countAnswers != 0:
        print lengthOrig, "\t", float(sumLength / countAnswers)
    else:
        print lengthOrig, "\t", 0
