#!/usr/bin/env python

import sys
import itertools

age_list = [line.strip().split("\t") for line in open("smalluser.txt")]

userlist = list()


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    instance = line.split()
    # increase counters
    userlist.append(instance)

dictionary = {}

for line in userlist:
    dictionary[line[0]] = (line[1],line[2])

for line in age_list:
    if line[0] in dictionary:
        age = line[2]
        clicks = dictionary[line[0]][0]
        impressions = dictionary[line[0]][1]
        print '%s\t%s\t%s' % (age,clicks,impressions)
