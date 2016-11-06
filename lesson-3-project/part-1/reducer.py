#!/usr/bin/python

import sys

numSales = 0
totalSales = 0.0
oldKey = None

# Loop around data
for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 2:
    # Something has gone wrong. Skip this line.
    continue
    
  thisKey, thisSale = data_mapped
  numSales += 1
  totalSales += float(thisSale)
  
 print numSales, "\t", totalSales
