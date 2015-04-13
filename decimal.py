#!/usr/bin/python

import sys

hexmap = {0:'0', 1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

def convert_number(val, divnum):

    quotient, remainder = divmod( val, divnum )

    while quotient != 0:

        yield remainder
        quotient, remainder = divmod( quotient, divnum )

    yield remainder

    return 


if len(sys.argv) == 2:
    int_string = sys.argv[1]

    dec = 0
    try:
        dec = int(int_string)

    except ValueError:
        sys.exit('Could not parse input to int')

    hexval = ''
    for val in convert_number(dec,16):
       hexval = hexmap[val] + hexval
    print hexval

    binaryval = ''
    for val in convert_number(dec,2):
       binaryval = str(val) + binaryval
    print binaryval

else:
    print 'No argument was given'


