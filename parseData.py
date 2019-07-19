"""
===============================================================================
Program to parse information from pre-collected data and store in a csv file
- sys.argv[1] = name of the csv file to be created
- sys.argv[2] = name of the subdirectory where the program will collect data 
- The .csv will have 4 categories:
    - row[0] = time
    - row[1] = average core usage
    - row[2] = RAM usage
    - row[3] = GPU Temperature
===============================================================================
"""
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
                        parseProcessInfo(newRow, timeStamp)
                        filewriter.writerow(newRow)

