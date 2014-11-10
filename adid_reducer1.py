#!/usr/bin/env python

import sys


current_adid = None
current_imp = 0
current_click = 0

for line in sys.stdin:
    # remove entrailing white spaces
    line = line.strip()

    adid, click, imp = line.split('\t')

    # convert to numbers
    try:
        click = int(click)
        imp = int(imp)

    # move on if it doesnt work
    except ValueError:
        continue

    # iterate
    if current_adid == adid:
        current_click += click
        current_imp += imp

    else:
        if current_adid:
            print '%s\t%s\t%s' % (current_adid, current_click, current_imp)
        current_adid = adid
        current_click = click
        current_imp = imp

# include last line
if current_adid:
    print '%s\t%s\t%s' % (current_adid, current_click, current_imp)
# output: 'adid \t clicks \t imp'