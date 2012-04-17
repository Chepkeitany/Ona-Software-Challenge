#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def __init__(self, **kwargs):
        self.variables=kwargs
        
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    
    def set_variable(self, k, v):
        self.variables[k]=v
    
    def get_variable(self, k):
        return self.variables.get(k, None)    

def main():
    donald = Duck(feet='purple')
    print(donald.get_variable('feet'))
    donald.set_variable('eyes', 'orange')
    print(donald.get_variable('eyes'))

if __name__ == "__main__": main()
