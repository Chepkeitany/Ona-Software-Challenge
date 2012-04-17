#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')
    
    def fur(self):
        print('I have feathers')
    
    def bark(self):
        print('You wish!')    
        
class Dog:
    def fur(self):
        print('I have brown and white fur')
    
    def bark(self):
        print('Woof!')
        
    def quack(self):
        print('That won''t happen for me am a dog stupid!')

    def walk(self):
        print('here goes, ... wait for it .. ''nope won''t happen.')   
         
def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.bark()
    
    bitch = Dog()
    bitch.bark()
    bitch.fur()
    bitch.walk()
    # point is if it can expose required function to asking object it implements polymorphism
    

if __name__ == "__main__": main()
