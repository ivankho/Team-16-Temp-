#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    adid, click, imp = line.split('\t')
    print '%s\t%s\t%s' % (adid, click, imp)