#!/usr/bin/python3
# switch.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    choices=dict(
                 a = 'A',
                 b = 'B',
                 c = 'C',
                 d = 'D',
    )
    v = 'x'
    print(choices.get(v,'other'))#can be used instead of using case
   

if __name__ == "__main__": main()
