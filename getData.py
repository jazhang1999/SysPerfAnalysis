#!/usr/bin/env python3

#import necessary libraries
import requests
from pprint import pprint as pp

URL = "http://127.0.0.1:8085/data.json"

r = requests.get(url = URL)

data = r.json()

pp(data)
