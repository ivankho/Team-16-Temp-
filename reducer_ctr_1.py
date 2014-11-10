#!/usr/bin/env python

from operator import itemgetter
import sys

current_UserID = None
current_impressions = 0
current_clicks =  0
UserID = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    UserID, clicks, impressions = line.split('\t')

    # convert count (currently a string) to int
    try:
        clicks = int(clicks)
        impressions = int(impressions)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_UserID == UserID:
        current_clicks += clicks
        current_impressions += impressions
    else:
        if current_UserID:
            # write result to STDOUT
            print '%s\t%s\t%s' % (current_UserID, current_clicks, current_impressions)
        current_clicks = clicks
        current_impressions = impressions
        current_UserID = UserID

# do not forget to output the last word if needed!
if current_UserID == UserID:
    print '%s\t%s\t%s' % (current_UserID, current_clicks, current_impressions)
