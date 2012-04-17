#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    n = 45
    s = 'This is a {} string!'.format(n)
    t = 'this is also a %s valid string' %n #python 2 so deprecated
    u = ''' this is also a valid python string'''
    v = """ \ 
triple quoted strings can span more than one line
like this and go on and on and on
""" # \ basically escapes the new line inserted at the end of the string
    print(s)

if __name__ == "__main__": main()
