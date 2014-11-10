#!/usr/bin/env python

import sys

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    instance = line.split()
    # increase counters
    print '%s\t%s\t%s' % (instance[11],instance[0],instance[1])
