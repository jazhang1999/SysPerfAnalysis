# SysPerfAnalysis
Python Program that analyzes CPU usage, temperature, and the top-running processes at any given time on the computer

# Three Step Process
We will require three steps to make this idea cohesive:
* Obtain the data (through python packages / implementations)
* Record the data (write into either a .json or .csv file)
* Perform data analysis of system performance (Visual representation, another python package)

Each one of these steps is a lot, but these are the main things to accomplish in order to make this process work. This will, as of now, also be done on a Windows 10 computer using the Ubuntu 18.04 virtual machine 

# Step One - getData.py 
Step one requires that we get the data. To do this required a two-pronged approach 
* We first obtained hardware data from Open Software Monitor by making it transmit to a private web server, then scraping the data off said web server in the form of a .json file (containing all the data on there)
* To get top processes running (measured by CPU usage), I first wrote and tested out a PowerShell script that would be able to retrieve the top 20 processes running on the PC at the time. I then incorporated this into my python code
`# Import necessary libraries
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
`
# Update (7/14/2019)
Obtaining the data is for the most part complete, with a couple of quality of life changes to come
* Hardware statistics - taken in as raw .json files in consistent intervals over a set amount of time
* Top running processes - taken in as raw .txt files during the same time as the hardware statistics
* For more information on the process, please read comments within getData.py

Notes
* I originally began this process of collection with psutil, a python library used for retrieving hardware data from the computer. This was eventually abandoned due to the fact that many of the modules I wanted to use were unavailable for my computer (limited linux and no Windows support being one of the bigger reasons why this was scrapped)
* This code was originally made to run off of my desktop (gaming) computer. If you would like to run this for yourself, then you will have to change the IP address where applicable
* For ease of testing and parsing, I made specific folders /dataFiles/ and /results/ to stash subdirectories of the pulled data in the former and the .csv files with the processed data in the latter. They are available for import but can be changed at the user's leisure

* To gain privileges to run Powershell commands from Linux vm: `Set-ExecutionPolicy RemoteSigned` (You might have to do this if this is your first time running the code. Run PowerShell x86 as administrator in order to execute this)
* The command line `ps | sort -desc cpu | select -first 20` is the code I used to access the top 20 processes on my computer. This can be modified, although be careful as this is not really a part of the rest of the Python code



