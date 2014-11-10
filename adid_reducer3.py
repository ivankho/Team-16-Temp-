#!/usr/bin/env python

import sys

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

    noclick = imp - click
    total_noclick = total_imp - total_click
    # calculate probabilities
    p_click = click/total_click
    p_noclick = noclick/total_noclick


    print '%s\t%s\t%s' % (adid, p_click, p_noclick)