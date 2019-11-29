#!/usr/bin/env python3
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
lista=[]
doc_id='0'
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    doc, word = line.split('\t', 1)
    if(doc_id!=doc):
       print ('%s\t%s' % (doc_id, lista))
       doc_id=doc
       lista=[]
    else:
     if(word in lista):
      pass
     else:
      lista.append(word)

print ('%s\t%s' % (doc_id, lista))
