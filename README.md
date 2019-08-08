# SysPerfAnalysis
Python Program that analyzes CPU usage, GPU Temperature, RAM usage, and the top-running processes at any given time on the computer. 

The idea behind this project was to test the limits of my new gaming PC that I had built this summer (2019). In most (if not all) of today's videogames, the manufacturer allows the user to adjust certain options or effects, either to improve the overall experience or lighten the load on the user's gaming device. For example, turning the graphics setting on Ultra will have a much higher load on the GPU than if the game was set to the Low graphics setting. Before the project, I had played games on it at the highest settings, but was concerned at how my computer was handling the load and if it would be better to drop to lower settings in order to let my computer handle a less intensive task. That is what inspired me to create working code that would record and later display data on CPU core usage, GPU temperature, and RAM usage in order to see how my computer would perform when forced to play different games operating under different settings. 

![Computer](Computer.png)

# Three Step Process
The project is broken down into three distinct steps:
* Step 1 - Periodically obtain the hardware performance and process statistics, then record them into files
* Step 2 - Process and parse the raw data obtained in Step 1 and record the desired information into a .csv file
* Step 3 - Present the data obtained in Step 2 in a visual format

This project was developed in Ubuntu 18.04 under Windows 10 WSL (Windows Subsystem for Linux), since it is possible to write code in a linux enviroment yet still run PowerShell commands.

# Step One - getData.py 
Step one requires that we get the PC performance data, which contains two parts: the hardware statistics, and the top running processes on the system.
* The user will first have to specify the name for where all the data will be saved. For example: `python3 getData.py sample1` will tell the program to save all the scraped data into a subdirectory within ./dataFiles/ into a subdirectory called sample1
* We first obtained hardware data from Open Hardware Monitor ([https://openhardwaremonitor.org/]). This software will run on the computer I wanted to test, and makes the hardware statistics available through a rest API. For my computer, the statistics are exposed at `http://192.168.1.18:8085/data.json`. The code periodically does HTTP GET and stores the .json file.
* To get top processes running (measured by CPU usage), I first wrote and tested out a PowerShell script that would be able to retrieve the top 20 processes running on the PC at the time. I then incorporated this into my python code to save the resulting output of that command into a .txt file
* Since one data pull gets both of the above at pretty much the exact same time, I simply named the resulting .json file and the .txt file with the timestamp when the reading took place (predetermined)

Note - I originally began this process of collection with psutil, a python library used for retrieving hardware data from the computer. This was eventually abandoned due to the fact that many of the modules I wanted to use were unavailable for my computer (limited linux and no Windows support being one of the bigger reasons why this was scrapped)

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

# Step 3 - graphData.py
Step 3 takes the .csv file created above and creates a graph of a selected field with respect to time
* The user will first have to specify the name of the .csv file that will be modelled into a graph. For example, the call `python3 graphData.py table1` will graph the .csv file named table1
* The user will then be prompted to this display, asking them to type in a number to select what they would like to see:

The 3 Avalialbe items to view are:
 1: CPU Core Usage
 2: RAM (Used Memmory)
 3: GPU Temperature
Enter the number of the option you want to run:

* The top running process at each time interval will be displayed with the time interval in question on the x-axis. The resulting graph will look something like this:
![Example Graph](exampleGraph.png)
 
* The new graph will be made into a .png, which will be named after the .csv file it was taken from and the option selected. For example, if the the graph was created with data from table1.csv and the user wanted to see the GPU Temperature, the resulting name would be `table1GPUTemperature.png`. The graph was first resized to fit the .png format, and then was saved to Windows Desktop for ease of viewing. If just the name is inputted, the resulting .png will show up in the current directory. 

* The resizing command (to make the graph fit) is `plt.tight_layout()`
* The command I used to put it on my Windows Desktop is `plt.savefig('/mnt/c/Users/Toby/Desktop/Graphs/' + sys.argv[1].split('.')[0] + readings[pickedOption - 1] + '.png')`

* _Originally, the program was designed to show the graph as a popup using the command plotmatlib.show(). However, due to limitations from using a WSL, this command does not work._ This will work, however, on a pure Windows system or MacOS, but for ease of use, the above process was chosen instead


# Additional Information
* This code was originally made to run off of my desktop (gaming) computer. If you would like to run this for yourself, then you will have to change the IP address and any directory paths where applicable
* For ease of testing and parsing, I made specific folders /dataFiles/ and /results/ to stash subdirectories of the pulled data in the former and the .csv files with the processed data in the latter. They are available for import but can be changed at the user's leisure
* To gain privileges to run Powershell commands from Linux vm: `Set-ExecutionPolicy RemoteSigned` (You might have to do this if this is your first time running the code. Run PowerShell x86 as administrator in order to execute this)
* The command line `ps | sort -desc cpu | select -first 20` is the code I used to access the top 20 processes on my computer. This can be modified, although be careful as this is not really a part of the rest of the Python code

# What I learned 
* __Making new directories via python / Navigation through WSL__ - Since this project involves a lot of data which is compiled in a lot of files, I realized there must be a better way to organize them. By learning how to make new directories and specify paths to retrieve files, I found this project to be much easier and well structured than anything I had previously done. It also gave me experience in navigating between the WSL and my actual Windows system, which was challenging at first but proved incredibly useful later on as the project got more and more complicated.
* __Windows Powershell__ - While I could get hardware information from Open Hardware Monitor, to get top running processes I needed to connect to the Windows software while still operating in WSL. Learning how to use Windows Powershell (allbeit very briefly) and tie it into my python program was an interesting experience, and introduced to me new ways of integrating many different systems to achieve a common goal.
* __CSV__ - For the third step of this project (visual representation), I needed to find a way to present a combination of .txt (processes) and .json (hardware information) files in a way so that my program could take the information and graph it easily. I found CSV to be very interesting to work with; with some of the sample code for writing a CSV file, I was able to quite easily able to make one. The real challenge was making sure everything went into the right place, and that I was retrieving and parsing the right information. 
* __PDB__ - As previously mentioned, one of the biggest challenges of this project was not really the organization or transfer of the data, but whether the right information was being pulled and put in the right place. Often during testing, I would find that the code would compile and work, but the readings produced would be entirely wrong. PDB (Python Debugger) was great for setting breakpoints where I could check to see the value of each variable and check what was really messing up the whole project. While I found it tough to learn at first, I think that using PDB saved me a lot of time in terms of checking to see what was wrong with the code.
* __matplotlib (Graphing)__ - I found that this was a very nice pacakge for graphing (for this project, I used the .pyplot extension). With some sample code and research (mostly on StackOverflow and GeeksForGeeks) I was able to produce a fairly legible graph after extensive debugging (problems with scaling and reading in the data in the correct order). However, this process was not without problems. One of the major issues that I personally had was that since I was using a WSL, I could not get the graph to render in a window due to system limitations. After testing that the graph would correctly render on my sibling's Macbook (MacOS), I decided to make it so that the program would render the graph as a .png and save it to my desktop with a very recognizable name that would tell the user exactly what they were looking at. 
* __Command line arguements__ - Even though this was not required to make the project work, I enjoyed using command line arguements to test my code. Instead of having to type every single time for user input, I just ran the same 3 to 4 commands in the shell to make sure everything was working as it should. Not the most critical aspect of this project, but definetely something fun to play around with. 

# Side notes
* Like with my previous project, one thing that I would definetely want to do is combine all three steps into one entity; that is, to make it so that the user would only need one command to make the entire process run. 




