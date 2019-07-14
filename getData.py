#!/usr/bin/env python3
"""
===============================================================================
Pulls out two different types of samples:
- samples on all of the statistics of the hardware, saved as a .json file
- the top 20 processes (in terms of cpu usage), saved as a .txt file

All these are pulled periodically, maybe plans to specify frequency and total
time in the future
===============================================================================
"""
# Import necessary libraries
import requests
import json
import time
from pprint import pprint as pp
from subprocess import check_output

# Server where data on hardware is transferred to
URL = "http://192.168.1.18:8085/data.json"

# Stores data from the above url in a .json format
r = requests.get(url = URL)
data = r.json()

# Sets the total time of reading to be 6 minutes (10 times 60 seconds)
t_end = time.time() + 60 * 10
while time.time() < t_end: 
	timeStamp = time.strftime('%Y-%m-%d-%H:%M:%S')
	with open('./dataFiles/' + timeStamp + '.json', 'w') as f:
    		json.dump(data, f)
	with open('./dataFiles/' + timeStamp + '.txt', 'w') as f:
		p = check_output(["powershell.exe", "ps | sort -desc cpu | select -first 20; exit"]).decode("utf-8")
		f.write(p)
		g = check_output(["powershell.exe", "exit"])
	pp("Collected a data file")
	time.sleep(10)


