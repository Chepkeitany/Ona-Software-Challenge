#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
from symbol import except_clause

def main():
    try:
#        fh = open('clines.txt')
        for line in openFile('lines.doc'): print(line.strip())
    except IOError as e:
        print('could not open file', e)
    except ValueError as e:
        print('Invalid file type selected', e)

def openFile(filename):
    if filename.endswith('.txt'):
        fh=open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
    

if __name__ == "__main__": main()
