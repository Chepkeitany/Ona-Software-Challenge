#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1,2,3, 4,5,6, eight= 8,nine=9,ten=10)

def testfunc(first,second,third,*args,**kwargs):
    print('Note the order of the argument passing. It is strict')
    print(first,second,third)
    for i in kwargs:
        print('unlimited entries')
        print(i, end=' \n')
    for i in args:
        print('name arguments')
        print(i, end=' ') 
        #N/B: These are very common for settings, flags, and combination with tuple arguments in programs

if __name__ == "__main__": main()
