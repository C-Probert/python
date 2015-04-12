#!/usr/bin/python

import sys
import string
import os.path
import readfile
from collections import Counter
#print 'Hello, World!'

#default file name
#check if file name is given as an arg
filename = 'thefile.txt'
if len(sys.argv) > 1:
    print 'argv[1] is {0}'.format(sys.argv[1])
    filename = sys.argv[1]

#get lines from file using readfile function
lines = readfile.get_lines(filename)

# counter is a subclass of dictionary which handles the occurances of the key
# https://docs.python.org/2/library/collections.html#collections.Counter
word_dict = Counter()

for line in lines:

    for word in line.strip('\n').split():

        wlow = word.strip('.,').lower()
        if wlow in word_dict:
            word_dict[wlow] += 1

        else:
            word_dict[wlow] = 1

mc = word_dict.most_common(1)[0]
print '{0} - {1}'.format(mc[0], mc[1])
