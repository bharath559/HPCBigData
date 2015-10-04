#!/usr/bin/env python

import sys
import os

input_file = os.getenv('map_input_file')
fileName = os.path.basename(input_file)
for line in sys.stdin:
        data = line.split()
        for key in data:
                print >>sys.stdout, "%s\t%s\t" % (key,fileName)
