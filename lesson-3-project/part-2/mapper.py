#!/usr/bin/python

# Mapper code for Part 2

import sys

for line in sys.stdin:
  data = line.strip().split(" ")
  if len(data) == 10:
    host, ident, authuser, date, timezone, request_type, page, request_protocol, status, bytes = data
    print "{0}\t{1}".format(page, bytes)
