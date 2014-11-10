#!/usr/bin/env python

import sys

# mapper 1
for line in sys.stdin:
    # remove entrailing white spaces
    line = line.strip()
    line = line.split('\t')
    print '%s\t%s\t%s' % (line[3], line[0], line[1])
    # output: 'adid \t click \t imp'
