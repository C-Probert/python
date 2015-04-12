#!/usr/bin/python

import sys
import string
import os.path

#default file name
#check if file name is given as an arg
def get_lines(filename):

    #make sure file is present
    if os.path.isfile(filename):

        print 'Found file: {0}'.format(filename)
        lines = []
        with open(filename, 'r') as file_obj:

            lines = list(file_obj)

        file_obj.closed
        return lines
    else:
        print 'Couldn\'t find file'
