#!/usr/bin/python3
# for.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    fh = open('lines.txt')
    for line in fh.readlines():#most common iteration code.also all containers in python are iterators
        print(line)
    i = 5    

if __name__ == "__main__": main()
