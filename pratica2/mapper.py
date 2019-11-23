#!/usr/bin/env python3
import sys
import re
tam=int(sys.argv[1])
atual=0
doc=-1
for line in sys.stdin:
    doc=doc+1
    while ((atual+tam)<len(line)): 
     shingle=line[atual:(atual+tam)]
     atual=atual+1
     print ('%s\t%s' % (shingle, 1)) 
  
      
     
