#!/usr/bin/python

import sys
import os.path
import zipfile
import string

filename = 'zipfile.zip'
if len(sys.argv) > 1:
    #print 'argv[1] is {0}'.format(sys.argv[1])
    filename = sys.argv[1]

if os.path.isfile(filename):

    with zipfile.ZipFile(filename) as zfile:

        #zfile.printdir()

        for finfo in zfile.infolist():
            #directories will always end with a /
            #to find the files, find the last / and split 
            # this will provide the file's name, the size can be found from the fileinfo object
            if not finfo.filename.endswith('/'):

                fname = finfo.filename.rsplit('/',1)
                size = '{0}\t{1}'.format( finfo.file_size, "B")

                #only going to go as far as gigabytes
                if finfo.file_size > 1024:

                    size = '{0:.2f}\t{1}'.format(finfo.file_size / 1024.0 , "KB")
                elif finfo.file_size > 1024 ** 2:

                    size = '{0:.2f}\t{1}'.format(finfo.file_size / (1024.0 ** 2) , "MB")

                elif finfo.file_size > 1024 ** 3:

                    size = '{0:.2f}\t{1}'.format(finfo.file_size / (1024.0 ** 3), "GB")

                print '{0}\t{1}'.format(fname[1], size)

    zfile.close()
else:
    print 'Couldn\'t find file'
