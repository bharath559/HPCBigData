#!/usr/bin/env python

import sys

last_key = None
running_total = None

for input_line in sys.stdin:
   input_line = input_line.strip()
   this_key, filename = input_line.split("\t", 1)

   if last_key == this_key:
       running_total = running_total+" "+ filename
   else:
       if last_key:
           print( "%s\t%s" % (last_key, running_total) )
       running_total = filename
       last_key = this_key

if last_key == this_key:
   print( "%s\t%s" % (last_key, running_total) )
