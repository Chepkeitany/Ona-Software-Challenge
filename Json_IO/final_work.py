#!/usr/bin/env python

try:
    #For use in Python 3 and above
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json


url = 'https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json'

#Function to take as input dataset from url
def calculate_waterpoints(url):
    """Receive the content of ``url``, parse it as JSON and return the
       object.
    """

    response = urlopen(url)
    data = str(response.read())
  
    #Working on looping through the dataset to return json object with the number of 
    # waterpoints that are functional and how many they are per community
    
    return json.load(response)
    #return json.loads(data)