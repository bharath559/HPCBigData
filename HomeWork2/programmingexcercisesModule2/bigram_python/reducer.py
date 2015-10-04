#!/usr/bin/env python
import sys

last_key = None
highest_key = None
running_total = 0
highest_total = 0
for input_line in sys.stdin:
	input_line = input_line.strip()
	this_key, value = input_line.split("\t", 1)
	value = int(value)

	if last_key == this_key:
		running_total += value
	else:
       		if running_total > highest_total:
			highest_total = running_total
			highest_key = last_key
		running_total = value
		last_key = this_key
print( "%s\t%d" % (highest_key, highest_total) )
