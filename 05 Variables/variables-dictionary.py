#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = {'one' :1, 'two' : 2, 'three' :3}
    for i in d:
        print(i, d[i])
#    print(type(d), d)
#another way to define a dictionary is 
    s = dict(
             one=1,two=2,three='three'# much easier right, use it this way
    )
    #add values to it this way
    s['seven'] = 7
    print(s)
if __name__ == "__main__": main()
