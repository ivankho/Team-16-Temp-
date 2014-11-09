#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    adid, click, imp, total_click, total_imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s' % (adid, click, imp, total_click, total_imp)