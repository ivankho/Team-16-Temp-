#!/usr/bin/env python

from operator import itemgetter
import sys

current_age = 0
current_clicks = 0
current_impressions =  0


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    age, clicks, impressions = line.split('\t')

    # convert count (currently a string) to int
    try:
        age = int(age)
        clicks = int(clicks)
        impressions = int(impressions)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_age == age:
        current_clicks += clicks
        current_impressions += impressions
    else:
        if current_age:
            # write result to STDOUT
            print '%s\t%s' % (current_age, (float(current_clicks)/float(current_impressions)))
        current_age = age
        current_clicks = clicks
        current_impressions = impressions

# do not forget to output the last word if needed!
if current_age == age:
    print '%s\t%s' % (current_age, (float(current_clicks)/float(current_impressions)))
