#!/usr/bin/env python

import sys

total_click = 0
total_imp = 0

for line in sys.stdin:
    # remove entrialing white spaces
    line = line.strip()

    adid, click, imp = line.split('\t')

    # turn to numbers
    try:
        click = int(click)
        imp = int(imp)

    # move on if bad data
    except ValueError:
        continue

    # cumulate total numbers
    total_click += click
    total_imp += imp
# print totals
print '%s\t%s' % (total_click, total_imp)