"""
===============================================================================
User input required as of now
===============================================================================
"""
# Import necessary libraries
import csv
import sys
import os
import json
import pdb

# Section to parse data and collect ===========================================

def parseHardwareInfo(mylist, nameOfFile):
        path = "./dataFiles/" + sys.argv[2] + "/" + nameOfFile + ".json"
        #print(">>> Opening file (%s)" % (path))
        with open(path, 'r') as json_file:
                data = json.load(json_file)
                #pdb.set_trace()

                Core1 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]
                Core2 = data['Children'][0]['Children'][1]['Children'][0]['Children'][1]['Value'].split()[0]
                Core3 = data['Children'][0]['Children'][1]['Children'][0]['Children'][2]['Value'].split()[0]
                Core4 = data['Children'][0]['Children'][1]['Children'][0]['Children'][3]['Value'].split()[0]
                Core5 = data['Children'][0]['Children'][1]['Children'][0]['Children'][4]['Value'].split()[0]
                Core6 = data['Children'][0]['Children'][1]['Children'][0]['Children'][5]['Value'].split()[0]

                CoreAVG = (float(Core1) + float(Core2) + float(Core3) + float(Core4) + float(Core5) + float(Core6)) / 6
                mylist.append(CoreAVG)
                ramMem = float(data['Children'][0]['Children'][2]['Children'][0]['Children'][0]['Value'].split()[0])
                mylist.append(ramMem)
                gpuTemp = float(data['Children'][0]['Children'][3]['Children'][1]['Children'][0]['Value'].split()[0])
                mylist.append(gpuTemp)

        # print(mylist)
        #print("The CPU core average load is " + str(CoreAVG) + " %")
        #print("The approximate RAM memmory usage is " + str(ramMem) + "%")
        #print("The approximate GPU temperature is " + str(gpuTemp) + " degrees Celsius")

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
        filewriter.writerow(['Time','CPU Core Usage', 'RAM Used Memmory', 'GPU Temperature', 'Top Running Process'])
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

