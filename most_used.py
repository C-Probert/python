#!/usr/bin/python

import sys
import string
import os.path
import readfile
from collections import Counter


#default file name
#check if file name is given as an arg
filename = 'thefile.txt'
if len(sys.argv) > 1:
    print 'argv[1] is {0}'.format(sys.argv[1])
    filename = sys.argv[1]

#get lines from file using readfile function
file_str = readfile.read_file(filename)

# counter is a subclass of dictionary that works well with keeping a count of its keys
# https://docs.python.org/2/library/collections.html#collections.Counter
word_dict = Counter()

for line in file_str.split('\n'):

    for word in line.split():
       
        #Don't want words that only differ with a period or a comma to cause the count to be off.
        #The assumption using strip is that periods and commas will fall into the correct grammatical placement on the end of a word.
        # if "words" could be a,b then replace would be a better choice
        wlow = word.strip('.,').lower()
        if wlow in word_dict:
            word_dict[wlow] += 1

        else:
            word_dict[wlow] = 1


mc = word_dict.most_common(1)[0]
#print key and value
print '{0} - {1}'.format(mc[0], mc[1])
