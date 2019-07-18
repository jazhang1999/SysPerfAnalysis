"""
===============================================================================
Graph the data in a legible way - specify which you want to see over time
- The x axis will display time (in minutes) and the top running process at 
  the given time in question
- For now, data points are hardlocked to include only every 10 second readings,
  with the full minutes being displayed on the x axis
- To view the graph on a linux-based OS, you need to install additional 
  packages and programs to be able to see it. (Fine for Win. and MacOS)
===============================================================================
"""

# Import the necessary libraries
import matplotlib.pyplot as plt
import csv
import sys
import pdb

# X and Y axis points (floats), declared as empty lists
x = []
y = []

# The actual labels that will appear for the x-axis
x_labels = []
readings = ['CPU Core Usage', 'RAM (Used Memmory)', 'GPU Temperature']

# Prompts for user input (determine what they want to see the progression of
print('The 3 Avalialbe items to view are:')
print('1: CPU Core Usage')
print('2: RAM (Used Memmory)')
print('3: GPU Temperature')

pickedOption = int(input('Enter the number of the option you want to run: '))

# Begins parsing in the data from the required csv fields in order to 
myTime = 0
with open( sys.argv[1], 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    
    for row in plots:
        if (myTime % 60 == 0):
            convertedTime = myTime / 60
            x_labels.append(str(convertedTime) + ' ' + row[len(row) - 1])
        else:
            x_labels.append(' ')
        x.append(myTime)
        y.append(float(row[pickedOption]))
        myTime += 10

# Displays the information after plotting it on the graph
plt.xlim(0, myTime)
plt.xticks(x, x_labels)
plt.xticks(rotation = 45)
plt.plot(x,y, label='Loaded over time')
plt.xlabel('Time (seconds)')
if (pickedOption == 1):
    plt.ylabel('Usage')
if (pickedOption == 2):
    plt.ylabel('Usage (in Megabytes)')
else:
    plt.ylabel('Temperature (degrees Celsius)')
plt.yscale('linear')
plt.title('Graph: ' + readings[pickedOption - 1] + ' over time (min)')
plt.legend(['Progression'], loc='upper left')
plt.show()

