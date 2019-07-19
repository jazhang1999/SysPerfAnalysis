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
* The user will first have to specify the name for where all the data will be saved. For example: `python3 getData.py sample1` will tell the program to save all the scraped data into a subdirectory within ./dataFiles/ into a subdirectory called sample1
* We first obtained hardware data from Open Software Monitor by making it transmit to a private web server, then scraping the data off said web server in the form of a .json file (containing all the data on there)
* To get top processes running (measured by CPU usage), I first wrote and tested out a PowerShell script that would be able to retrieve the top 20 processes running on the PC at the time. I then incorporated this into my python code to save the resulting output of that command into a .txt file
* Since one data pull gets both of the above at pretty much the exact same time, I simply named the resulting .json file and the .txt file with the timestamp when the reading took place (predetermined)
* For more individual documentation on specific lines of code, please see below:

```
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
```
# Step 2 - parseData.py
Step two requires that we parse the data and put it into a .csv file to make it graphable (viewable)
* The user will first have to specify the name of the .csv file to be created, and then the directory where the data is stored. For example, the call `python3 parseData.py table1 sample1` will tell the program to make a .csv file named table1 to pull data from the directory sample1
* First I had to make the .csv file. I put mine into a folder called /results/ just for organization
* Next, I specified, then opened, the directory where all my data was (the .json from Open Hardware Monitor and the .txt from the PowerShell command)
* From there, I specified the first row of the .csv file to be the column names 
* Then, I just iterated through all the .json files, and called the .txt files by splicing out the timestamp of a .json's name and adding '.txt' to access its corresponding .txt file
* By the end, the resulting data would look something like this:

Time|CPU Core Usage|RAM Used Memmory|GPU Temperature|Top Running Process
|---|---|---|---|---|
2019-07-15-22:10:11|8.016666666666667|25.9|43.0|Steam

```
# Import necessary libraries
import csv
import sys
import os
import json
import pdb

# Section to parse data and collect ===========================================
# Pulls data from the .json file (Open Hardware Monitor information)
def parseHardwareInfo(mylist, nameOfFile):
        path = "./dataFiles/" + sys.argv[2] + "/" + nameOfFile + ".json"
        with open(path, 'r') as json_file:
                data = json.load(json_file)
                # I pulled the average core usage, RAM usage, and GPU Temperature, in that order
                CoreAVG = float(data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0])
                mylist.append(CoreAVG)
                ramMem = float(data['Children'][0]['Children'][2]['Children'][0]['Children'][0]['Value'].split()[0])
                mylist.append(ramMem)
                gpuTemp = float(data['Children'][0]['Children'][3]['Children'][1]['Children'][0]['Value'].split()[0])
                mylist.append(gpuTemp)

def parseProcessInfo(mylist, nameOfFile):
        f = open("./dataFiles/" + sys.argv[2] + "/" + nameOfFile + ".txt", "r")
        rawText = f.read()
        topProcessLine = rawText.split("\n")[3].split()
        topProcess = topProcessLine[len(topProcessLine) - 1]
        mylist.append(topProcess)

# Specify the path for the new CSV file
path = "./results/" + sys.argv[1] + ".csv"

# Specify where the data for processing is
directory = os.fsencode("./dataFiles/" + sys.argv[2])

# Create the CSV file that will be stored (Chosen name)
with open(path, 'w') as csvfile:
        filewriter = csv.writer(csvfile)
        # Write the first row to be the headers for each column in the .csv
        filewriter = csv.writer(csvfile)
        filewriter.writerow(['Time','CPU Core Usage', 'RAM Used Memmory', 'GPU Temperature', 'Top Running Process'])
        # Now we can loop through the rest of the data and input it into the .csv
        for fn in os.listdir(directory):
                filename = os.fsdecode(fn)
                if filename.endswith(".json"):
                        timeStamp = filename.split(".")[0]
                        newRow = []
                        newRow.append(timeStamp)
                        #pdb.set_trace()
                        parseHardwareInfo(newRow, timeStamp)
                        #pdb.set_trace()
```

# Notes
* I originally began this process of collection with psutil, a python library used for retrieving hardware data from the computer. This was eventually abandoned due to the fact that many of the modules I wanted to use were unavailable for my computer (limited linux and no Windows support being one of the bigger reasons why this was scrapped)
* This code was originally made to run off of my desktop (gaming) computer. If you would like to run this for yourself, then you will have to change the IP address where applicable
* For ease of testing and parsing, I made specific folders /dataFiles/ and /results/ to stash subdirectories of the pulled data in the former and the .csv files with the processed data in the latter. They are available for import but can be changed at the user's leisure

* _The graph will not work on Ubuntu based systems. The code will compile, but the resulting graph will not display_. You can run it on MacOS or through Windows PowerShell (for windows, I moved everything to the desktop and rewrote some of the paths in the original code. I would not recomend this to be a permanent setup unless for testing). MacOS seems to work fine without any real problems.
* Alternatively, this link [https://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/] will show you how to change certain things in Ubuntu to make it work. I did not do it because I'm new to linux as a whole, but for more experienced people this will work for them

* To gain privileges to run Powershell commands from Linux vm: `Set-ExecutionPolicy RemoteSigned` (You might have to do this if this is your first time running the code. Run PowerShell x86 as administrator in order to execute this)
* The command line `ps | sort -desc cpu | select -first 20` is the code I used to access the top 20 processes on my computer. This can be modified, although be careful as this is not really a part of the rest of the Python code

# Future Plans (as of 7/19/19)
* Make it all encompassing (one program to do all three steps)




