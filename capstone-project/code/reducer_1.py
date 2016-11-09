#!/usr/bin/python

import sys

hourString = ""
oldKey = None
counter_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour =  data_mapped

    # new user so it is time to print the old user's highest-posting hour(s)
    if oldKey and oldKey != thisKey:
        # the hours this user posted and how many posts for that hour
        hourList = hourString.split(",")
        for hour in hourList:
            if hour in counter_dict:
                counter_dict[hour] += 1
            else:
                counter_dict[hour] = 1
        max_count = max(counter_dict.values())
        # print the hours the maximum posts per hour occurred
        for hour, count in counter_dict.iteritems():
            if count == max_count:
                print oldKey[1:-1], "\t", hour[1:-1]
        # reset the user and the list of hours that user posted
        oldKey = thisKey
        hourString = ""
        counter_dict = {}

    oldKey = thisKey
    # add another hour the the list of the hours that user posted
    if hourString == "":
        hourString = thisHour
    else:
        hourString += "," + thisHour

# print the last line
if oldKey != None:
    # the hours this user posted and how many posts for that hour
    hourList = hourString.split(",")
    for hour in hourList:
        if hour in counter_dict:
            counter_dict[hour] += 1
        else:
            counter_dict[hour] = 1
    max_count = max(counter_dict.values())
    # print the hours the maximum posts per hour occurred
    for hour, count in counter_dict.iteritems():
        if count == max_count:
            print oldKey[1:-1], "\t", hour[1:-1]

