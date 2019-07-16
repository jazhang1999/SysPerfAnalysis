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

# Section to parse data and collect ===========================================

def parseCSV(mylist, nameOfFile):
        with open("./dataFiles/" + sys.argv[2] + "/" + nameOfFile + ".json", 'r') as json_file:
                data = json.load(json_file)

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

        #print("The CPU core average load is " + str(CoreAVG) + " %")
        #print("The approximate RAM memmory usage is " + str(ramMem) + "%")
        #print("The approximate GPU temperature is " + str(gpuTemp) + " degrees Celsius")

def parseTXT(mylist, nameOfFile):
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
	# Is this a list?	
	filewriter.writerow(['Time', 'GPU Temperature', 'CPU Core Usage', 'RAM Used Memmory', 'Top Running Process'])
	for file in os.listdir(directory):
		filename = os.fsdecode(file)
		if filename.endswith(".json"):
			timeStamp = filename.split(".")[0]
			newRow = []
			newRow.append(timeStamp)
			parseCSV(newRow, timeStamp)
			parseTXT(newRow, timeStamp)
			filewriter.writerow(newRow)

# Section to parse data and collect ===========================================

def parseCSV(mylist, nameOfFile):
	with open(nameOfFile + ".json", 'r') as json_file:
        	data = json.load(json_file)

	Core1 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]
	Core2 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]
	Core3 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]
	Core4 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]
	Core5 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]
	Core6 = data['Children'][0]['Children'][1]['Children'][0]['Children'][0]['Value'].split()[0]

	CoreAVG = (float(Core1) + float(Core2) + float(Core3) + float(Core4) + float(Core5) + float(Core6)) / 6
	mylist.append(CoreAVG)
	ramMem = float(data['Children'][0]['Children'][2]['Children'][0]['Children'][0]['Value'].split()[0])
	mylist.append(ramMem)
	gpuTemp = float(data['Children'][0]['Children'][3]['Children'][1]['Children'][0]['Value'].split()[0])
	mylist.append(gpuTemp)
		
	#print("The CPU core average load is " + str(CoreAVG) + " %")
	#print("The approximate RAM memmory usage is " + str(ramMem) + "%")
	#print("The approximate GPU temperature is " + str(gpuTemp) + " degrees Celsius")

def parseTXT(mylist, nameOfFile):
	f = open(nameOfFile + ".txt", "r")
	rawText = f.read()
	topProcessLine = rawText.split("\n")[3].split()
	topProcess = topProcessLine[len(topProcessLine) - 1]
	mylist.append(topProcess)
