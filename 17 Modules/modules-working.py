#!/usr/bin/python3
# modules.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sys
import bitstring

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    print(sys.prefix)
    
#    import os
#    print(os.name)
#    print(os.getenv('PATH'))
#    print(os.urandom(20))
    
#    import urllib.request
#    page=urllib.request.urlopen('http://www.bw.org/')
#    print(page)
#    for line in page: print(str(line, encoding='utf_8'),end='')
   
#    import random
#    print(random.randint(1,9999999))
    
#    import datetime
#    tariki=datetime.datetime.now()
#    print(tariki.month, tariki.day, tariki.year)

    
    a = bitstring.BitArray('0x1af')
    print(a.hex, a.bin, a.uint)

if __name__ == "__main__": main()
