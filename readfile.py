#!/usr/bin/python

import sys
import string
import os.path

#class is used as a library to read a file and place its contents into a string. 
#since not all py files expect the results to be broken up by newline chars, we'll just return the string 
#and defer to the other py files

def read_file(filename):

    #make sure file is present
    if os.path.isfile(filename):

        #print 'Found file: {0}'.format(filename)
        file_str = ''
        with open(filename, 'r') as file_obj:

            #this isn't optimal for large files 
            #short of reading the file a char at a time, this is the best choice
            file_str = file_obj.read()

        file_obj.closed
        return file_str
    else:
        print 'Couldn\'t find file'
        sys.exit()
        
