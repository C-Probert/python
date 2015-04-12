#!/usr/bin/python

import sys
import string
import os.path
from collections import Counter
#print 'Hello, World!'

#default file name
#check if file name is given as an arg
filename = 'thefile.txt'
if len(sys.argv) > 1:
    print 'argv[1] is {0}'.format(sys.argv[1])
    filename = sys.argv[1]

print filename

#make sure file is present
if os.path.isfile(filename):

    print 'Found file: {0}'.format(filename)

    # counter is a subclass of dictionary which handles the occurances of the key
    # https://docs.python.org/2/library/collections.html#collections.Counter
    word_dict = Counter()
    
    with open(filename, 'r') as file_obj:

        # Read line, split on whitespace 
        # If word is not present in dictionary, insert, otherwise update value of dictionary (count)

        for line in file_obj:
            
            for word in line.strip('\n').split():
               
                wlow = word.strip('.,').lower()
                if wlow in word_dict:
                    word_dict[wlow] += 1
                    
                else:
                    word_dict[wlow] = 1

    file_obj.closed
    #c_word = word_dict.most_common(1)[0]
    #print '{0} - {1}'.format(c_word[0],c_word[1])
    print word_dict.most_common()


else:
    print 'Couldn\'t find file'
