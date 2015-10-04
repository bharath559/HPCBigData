#!/usr/bin/env python
import sys
 
for line in sys.stdin:
	data = line.split()
	if len(data) < 3:
        	continue
    	i = 0
	for key in data:
		if len(data) == i+1:
			continue
		print >>sys.stdout, "%s\t%d" % (key+" "+data[i+1],1)
		i=i+1
