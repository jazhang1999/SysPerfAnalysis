# SysPerfAnalysis
Python Program that analyzes CPU usage, temperature, and the top-running processes at any given time on the computer

# Three Step Process
We will require three steps to make this idea cohesive:
* Obtain the data (through python packages / implementations)
* Record the data (write into either a .json or .csv file)
* Perform data analysis of system performance (Visual representation, another python package)

Each one of these steps is a lot, but these are the main things to accomplish in order to make this process work

# Update (7/14/2019)
Obtaining the data is for the most part complete, with a couple of quality of life changes to come
* Hardware statistics - taken in as raw .json files in consistent intervals over a set amount of time
* Top running processes - taken in as raw .txt files during the same time as the hardware statistics

Process:
* The user will run the program getData.py
* There should also be a preexisting directory called dataFiles, where all the output dumps to
* A .json file and .txt file (see above for more details) will be set into the dataFiles directory each interval in a given amount of time 
* Once the program ends, dataFiles should contain all the data that is needed to process for that sampling period

