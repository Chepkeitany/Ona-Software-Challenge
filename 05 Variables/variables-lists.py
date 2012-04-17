#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    x = (1, 2, 3 )
    y = [1, 2, 3]
    y.append(7)
    
#    z = 'string' #this is also another type of list
#    print(type(z),z[2:4])
#    print(type(x), x)
#    print(type(y), y)
    
    #use case in control structures
    for i in y:
        print(i)
    
if __name__ == "__main__": main()
