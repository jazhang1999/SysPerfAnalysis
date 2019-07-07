# import the necessary modules

import csv
Name = "Donald Trump"

with open('test.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row[1])
