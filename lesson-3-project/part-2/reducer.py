#!/usr/bin/python

import sys

numHits
oldKey = None

# Loop around data
for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    # Something has gone wrong. Skip this line.
    continue
  
  # If the keys, which are in alphabetical order, have changed
  if oldKey and oldKey != thisKey:
    print oldKey, "\t", numHits
    numHits = 0
  
  numHits += 1
  oldKey = thisKey

# Print last line
if oldKey != None:
  print oldKey, "\t", numHits
