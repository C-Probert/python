#!/usr/bin/python

import sys
import os.path
import readfile

alphabet =  {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7,
             'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14,
             'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 
             'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
             
filename = 'thefile.txt'
if len(sys.argv) > 1:
    filename = sys.argv[1]


file_str = readfile.read_file(filename)
lines = file_str.split('. ');

highest = 0,''
#break each line up into sentences
for line in lines:

    #sline = line.replace('\n','')
    #print 'sline={0}'.format(sline)

    line_amount = 0

    for l_char in line :

        #making the assumption that the encoding of the file is ascii
        #if unicode support is needed, unichr() function can be used
        #ignore char unless it falls in the range of a-z or A-Z

        num = ord(l_char)
        if( (num >= 65 and num <= 90) or (num >= 97 and num <= 122) ):

            line_amount += alphabet[l_char.lower()]

            
    #print 'sline count={0}'.format(line_amount)
    if line_amount > highest[0] :
        highest = line_amount, line

print 'Highest sentence: {0} - {1}'.format(highest[1],highest[0])
            

