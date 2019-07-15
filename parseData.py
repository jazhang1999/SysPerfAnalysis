

import csv

# Create the CSV file that will be stored (Chosen name)
with open('test.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',' quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Time', 'GPU Temperature', 'CPU Core Usage', 'RAM Used Memmory'])

    
# Section to parse data and collect ===========================================

