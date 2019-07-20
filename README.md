# SysPerfAnalysis
Python Program that analyzes CPU usage, temperature, and the top-running processes at any given time on the computer.

# Three Step Process
We will require three steps to make this idea cohesive:
* Obtain the data (through python packages / implementations)
* Record the data (write into either a .json or .csv file)
* Perform data analysis of system performance (Visual representation, another python package)

Each one of these steps is a lot, but these are the main things to accomplish in order to make this process work. This will, as of now, also be done on a Windows 10 computer using the Ubuntu 18.04 virtual machine. 

# Step One - getData.py 
Step one requires that we get the PC performance data, which contains two parts: the hardware statistics, and the top running processes on the system.
* The user will first have to specify the name for where all the data will be saved. For example: `python3 getData.py sample1` will tell the program to save all the scraped data into a subdirectory within ./dataFiles/ into a subdirectory called sample1
* We first obtained hardware data from Open Hardware Monitor ([https://openhardwaremonitor.org/]). This software will run on the computer I wanted to test, and makes the hardware statistics available through a rest API. For my computer, the statistics are exposed at `http://192.168.1.18:8085/data.json`. The code periodically does HTTP GET and stores the .json file.
* To get top processes running (measured by CPU usage), I first wrote and tested out a PowerShell script that would be able to retrieve the top 20 processes running on the PC at the time. I then incorporated this into my python code to save the resulting output of that command into a .txt file
* Since one data pull gets both of the above at pretty much the exact same time, I simply named the resulting .json file and the .txt file with the timestamp when the reading took place (predetermined)

# Step 2 - parseData.py
Step two requires that we parse the data and put it into a .csv file to make it graphable (viewable)
* The user will first have to specify the name of the .csv file to be created, and then the directory where the data is stored. For example, the call `python3 parseData.py table1 sample1` will tell the program to make a .csv file named table1 to pull data from the directory sample1.

* The program must iterate through all files within the above mentioned subdirectory. 
* In order to obtain CPU Core Usage, RAM Used Memmory, GPU Temperature, the program accesses each .json files collected in Step 1 and go through the JSON heirarchy to obtain the elements needed.
* In order to obtain the Top Process, the program accesses the corresponding .txt file (with the top processes) and parses out the name of the top running process.
* All the parsed results (.csv files) will be put into a separate subdirectory `./results/`
* The first row of the .csv file was to be the column names

* By the end, the resulting data would look something like this:
Time|CPU Core Usage|RAM Used Memmory|GPU Temperature|Top Running Process
|---|---|---|---|---|
2019-07-15-22:10:11|8.016666666666667|25.9|43.0|Steam


# Notes
* I originally began this process of collection with psutil, a python library used for retrieving hardware data from the computer. This was eventually abandoned due to the fact that many of the modules I wanted to use were unavailable for my computer (limited linux and no Windows support being one of the bigger reasons why this was scrapped)
* This code was originally made to run off of my desktop (gaming) computer. If you would like to run this for yourself, then you will have to change the IP address where applicable
* For ease of testing and parsing, I made specific folders /dataFiles/ and /results/ to stash subdirectories of the pulled data in the former and the .csv files with the processed data in the latter. They are available for import but can be changed at the user's leisure
============================================================================
* _The graph will not work on Ubuntu based systems. The code will compile, but the resulting graph will not display_. You can run it on MacOS or through Windows PowerShell (for windows, I moved everything to the desktop and rewrote some of the paths in the original code. I would not recomend this to be a permanent setup unless for testing). MacOS seems to work fine without any real problems.
* Alternatively, this link [https://www.pyimagesearch.com/2015/08/24/resolved-matplotlib-figures-not-showing-up-or-displaying/] will show you how to change certain things in Ubuntu to make it work. I did not do it because I'm new to linux as a whole, but for more experienced people this will work for them
============================================================================
* To gain privileges to run Powershell commands from Linux vm: `Set-ExecutionPolicy RemoteSigned` (You might have to do this if this is your first time running the code. Run PowerShell x86 as administrator in order to execute this)
* The command line `ps | sort -desc cpu | select -first 20` is the code I used to access the top 20 processes on my computer. This can be modified, although be careful as this is not really a part of the rest of the Python code

# Future Plans (as of 7/19/19)
* Make it all encompassing (one program to do all three steps)




