#!/usr/bin/env python3
import sys
import re
for line in sys.stdin:
    line = line.strip()
    line = line.split('=' )
    words = line.split('\\' )
    for word in words:
     print ('%s\t%s' % (word, 1))
