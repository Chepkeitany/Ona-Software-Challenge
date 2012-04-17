#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = 'test for an occurence of line in line one line'
    for i,c in enumerate(fh): #the i here is an index, it works like the counter in a normal for loop
        if c == 'l':
            print('index {} is an occurence of the word line '.format(i) )

if __name__ == "__main__": main()
