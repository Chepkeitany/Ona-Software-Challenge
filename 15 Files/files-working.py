#!/usr/bin/python3
# files.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def binaryReadandWrite(filehandle):
    #function accepts a binary filehandle and makes a copy of the file in filehandle
    
    buffersize = 50000
    infile=filehandle
    outfile=open('newfile.jpg','wb')
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = ' ')
        buffer=infile.read(buffersize)
    print()
    print('Done copying file')
    
def main():
    buffersize=50000
    infile = open('lines.txt','r')
    outfile= open('copy1-lines.txt', 'w')
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end = '')
        buffer=infile.read(buffersize)
    print()
    print('Done.')
    
    newinfile=open('olives.jpg','rb')
    binaryReadandWrite(newinfile)

if __name__ == "__main__": main()
