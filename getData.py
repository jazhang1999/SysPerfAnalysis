#!/usr/bin/env python3

#import necessary libraries
import requests
import json

from pprint import pprint as pp

URL = "http://192.168.1.18:8085/data.json"

r = requests.get(url = URL)

data = r.json()

with open('./data.json', 'w') as f:
    json.dump(data, f)

#pp(data)
pp("This data has been saved to a local file (or rewritten)");

