#!/usr/bin/env python3
import sys
import re
import hashlib
tam=int(sys.argv[1])
b=int(sys.argv[1])
atual=0
doc=-1
def string2numeric_hash(text):
    import hashlib
    return int(hashlib.md5(text).hexdigest()[:8], 16)
 
for line in sys.stdin:
    doc=doc+1
    while ((atual+tam)<len(line)): 
     h = hashlib.sha1()
     shingle=line[atual:(atual+tam)]
     shingle=shingle.encode('utf-8')
     atual=atual+1
     print ('%s\t%s' % (doc, string2numeric_hash(shingle))) 
  
     
