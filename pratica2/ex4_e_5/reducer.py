#!/usr/bin/env python3
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
lista={}
lista_aux=[]
lista_final=[]
doc_id='0'
# input comes from STDIN
for line in sys.stdin:
    lista_aux=[]
    line = line.strip()
    doc, word = line.split('\t', 1)
    if(doc_id!=doc):
       lista[doc_id]=lista_aux
       doc_id=doc
       lista_aux=[]
    else:
     if(word in lista):
      pass
     else:
      lista_aux.append(word)

for i in lista:
 for j in lista:
  if(j!=i):
    lista_final = [x for x in i if x not in j]
    print ('[%s\t%s]\t%s' % (i, j, len(lista_final)-len(i)))
