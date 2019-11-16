from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
count_aux=[]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    current_count=[]
    # parse the input we got from mapper.py
    word, count = line.split("\t")
    count_aux.append(count)
print ('%s\t%s' % ( word, str(count_aux)))
