#!/usr/bin/env python3
import sys
import re
import fileinput
import os

for filename in os.listdir("/home/hadoop/hadoop-master/pratica1/map_reducer_py/input/"):
    for words in open("/home/hadoop/hadoop-master/pratica1/map_reducer_py/input/"+filename):
     emails = re.findall(r'\d{16}', words)
     for email in emails:	
       if(filename!=email):
        print ('%s\t%s' % (filename,email))
