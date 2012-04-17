#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc('cute')
    empty()
    anotherFunc(12, 25, 60, 58, 63, 85)

def testfunc(n=0):
    print('This is a test function',n)
#functions must have content. use pass as a place holder
def empty():
    pass
def anotherFunc(a,b,c, *args):#user *args to allow fucntions to accept unlimited number
    #of arguments. will be tuple
    print(a,b,c)
    for i in args:
        print(i, end=' ')

if __name__ == "__main__": main()
