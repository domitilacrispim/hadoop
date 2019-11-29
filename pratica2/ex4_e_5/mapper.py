#!/usr/bin/env python3
import sys
import re
import hashlib
from random import randint	
a=int(sys.argv[1])
n=int(sys.argv[2])
p=int(sys.argv[3])

def hash_doido(shingle, n, p):
  aux = int(hashlib.sha256(shingle.encode('utf-8')).hexdigest(), 16) % 10**8
  aux=aux+n
  aux=aux-p*randint(1, 1000000)
  aux=abs(aux*(n-p))
  return aux
  

for line in sys.stdin:
    lista=[]
    doc, word = line.split('\t', 1)
    for i in range (0, a):
      mim=35563243242332730878756754324
      for c in word:
       if(mim> hash_doido(c, n, p)):
         mim=hash_doido(c, n, p)
      lista.append(mim) 
    print ('%s\t%s' % (doc,lista)) 
  
     
