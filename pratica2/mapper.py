#!/usr/bin/env python3
import sys
import re
list_sh=[]
tam=int(sys.argv[1])
atual=0
comeco=0
for line in sys.stdin:
    while ((atual+tam)<len(line)): 
     shingle=line[atual:(atual+tam)]
     if(shingle in list_sh):
      atual=atual+1
     else:
      list_sh.append(shingle)
      atual=atual+1
for word in list_sh:
  print ('%s\t%s' % (word, 1)) 
     
      
     
