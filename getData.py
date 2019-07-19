#!/usr/bin/env python3
"""
===============================================================================
Pulls out two different types of samples:
- samples on all of the statistics of the hardware, saved as a .json file
- the top 20 processes (in terms of cpu usage), saved as a .txt file
- for now, the user can specify a time limit (in minutes) and a reading will be
  pulled every 10 seconds (User will be prompted to do so at available time
- All the data will be dumped into a subdirectory under ./dataFiles for ease
  of parsing in the future. The user will choose the subdirectory name

All these are pulled periodically, maybe plans to specify frequency and total
time in the future
===============================================================================
"""
# Import necessary libraries
import sys
import os
import requests
import json
import time
from pprint import pprint as pp
from subprocess import check_output

# sys.argv[1] will be the name for which all the pulled data will be stored
dirname = "./dataFiles/" + sys.argv[1]
if not os.path.exists(dirname):
        os.mkdir(dirname)
else:
        print("Directory name already exists, pick a new one please")
        sys.exit(1)

# Server where data on hardware is transferred to
URL = "http://192.168.1.18:8085/data.json"

readingPeriod = int(input('How long should this collection process be? (in minutes): '))

# Sets the total time of reading to be x minutes (x times 60 seconds)
t_end = time.time() + 60 * readingPeriod
while time.time() < t_end: 
        timeStamp = time.strftime('%Y-%m-%d-%H:%M:%S')
        
        # Stores data from the above url in a .json format
        r = requests.get(url = URL)
        data = r.json()
        with open(dirname + "/" + timeStamp + '.json', 'w') as f:
                json.dump(data, f)

        # Collect top 20 processes by CPU usage
        with open(dirname + "/" + timeStamp + '.txt', 'w') as f:
                p = check_output(["powershell.exe", "ps | sort -desc cpu | select -first 20; exit"]).decode("utf-8")
                f.write(p)
                g = check_output(["powershell.exe", "exit"])
        pp("Collected a data file")
        time.sleep(10)


