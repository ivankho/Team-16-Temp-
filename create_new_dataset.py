#!/usr/bin/env python

import sys

# artifically create new text file with total clicks and imps
for line in open('reducer2_output.txt'):
    line = line.strip()
    total_click, total_imp = line.split('\t')
for line in open('reducer1_output.txt'):
    line = line.strip()
    adid, click, imp = line.split('\t')
    print '%s\t%s\t%s\t%s\t%s' % (adid, click, imp, total_click, total_imp)