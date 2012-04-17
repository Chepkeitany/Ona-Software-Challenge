#!/usr/bin/python3
# generator.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for i in inclusiveRrange(1,100,3.5,53):
        print(i, end = ' ')

def inclusiveRange(*args):
    numargs=len(args)
    if numargs<1:
        raise TypeError('must supply at least one argument')
    elif numargs==1:
        start=0
        step=1
        stop=args[0]
    elif numargs==2:
        (start,stop) = args
        step=1
    elif numargs==3:
        (start,stop,step)= args
    else:
          raise TypeError('inclusive range at most 3 arguments, got {}'.format(numargs))  
    i=start
    while i <= stop:
        yield i #this ensures execution begins here after first function call
        i +=step
    

if __name__ == "__main__": main()
