#!/usr/bin/env python

import sys

# mapper 1
for line in sys.stdin:
    # remove entrailing white spaces
    line = line.strip()
    line = line.split('\t')
    print '%s\t%s\t%s' % (line[3], line[0], line[1])
    # output: 'adid \t click \t imp'

# reducer 1

current_adid = None
current_imp = 0
current_click = 0

for line in sys.stdin:
    # remove entrailing white spaces
    line = line.strip()

    adid, click, imp = line.strip('\t')

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


# reducer 2
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

# artifically create new text file with total clicks and imps
for line in open('reducer2_output.txt'):
    line = line.strip()
    total_click, total_imp = line.split('\t')
for line in open('reducer1_output.txt'):
    line = line.strip()
    adid, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s' % (adid, click, imp, total_click, total_imp)

# create mapper for new data file
# not sure if even necessary...
for line in sys.stdin:
    line = line.strip()
    adid, click, imp, total_click, total_imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s' % (adid, click, imp, total_click, total_imp)

# reducer for new data file
current_adid = None

for line in sys.stdin:
    # remove entrailing white spaces
    line = line.strip()
    adid, click, imp, total_click, total_imp = line.split('\t')

    # convert to numbers
    try:
        click = float(click)
        imp = float(imp)
        total_click = float(total_click)
        total_imp = float(total_imp)

    # move on if bad data
    except ValueError:
        continue

    # remember that everything is already aggregated
    if current_adid == adid:
        noclick = imp - click
        total_noclick = total_imp - total_click
        # calculate probabilities
        p_click = click/total_click
        p_noclick = noclick/total_noclick

    else:
        if current_adid:
            print '%s\t%s\t%s' % (current_adid, p_click, p_noclick)
        current_adid = adid

# don't forget final line
if current_adid:
    print '%s\t%s\t%s' % (current_adid, p_click, p_noclick)