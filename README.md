# SysPerfAnalysis
Python Program that analyzes CPU usage, temperature, and the top-running processes at any given time on the computer

# Three Step Process
We will require three steps to make this idea cohesive:
* Obtain the data (through python packages / implementations)
* Record the data (write into either a .json or .csv file)
* Perform data analysis of system performance (Visual representation, another python package)

Each one of these steps is a lot, but these are the main things to accomplish in order to make this process work. This will, as of now, also be done on a Windows 10 computer using the Ubuntu 18.04 virtual machine 

# Update (7/14/2019)
Obtaining the data is for the most part complete, with a couple of quality of life changes to come
* Hardware statistics - taken in as raw .json files in consistent intervals over a set amount of time
* Top running processes - taken in as raw .txt files during the same time as the hardware statistics
* For more information on the process, please read comments within getData.py

Notes
* I originally began this process of collection with psutil, a python library used for retrieving hardware data from the computer. This was eventually abandoned due to the fact that many of the modules I wanted to use were unavailable for my computer (limited linux and no Windows support being one of the bigger reasons why this was scrapped)
* To obtain data about hardware (CPU usage, GPU temperature, RAM usage, etc.) I instead used a program called Open Hardware Monitor, which can be set up to project all my computer data to its own web server. From the web server, it is possible to extract an extension of all that data in a .json form. Due to its flexibility, I decided to make this the main way to obtain data about hardware on my computer
* To get top processes running (measured by CPU usage), I first wrote a PowerShell script, then after unlocking certain privileges (which I will include at the bottom), I wrote for the same PowerShell command to be run from a python program in a linux setting. 
* Any further documentation can be found in the actual getData.py code

* To gain privileges to run Powershell commands from Linux vm: `Set-ExecutionPolicy RemoteSigned` (You might have to do this if this is your first time running the code. Run PowerShell x86 as administrator in order to execute this)
* The command line `ps | sort -desc cpu | select -first 20` is the code I used to access the top 20 processes on my computer. This can be modified, although be careful as this is not really a part of the rest of the Python code



