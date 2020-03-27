import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('', '', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    i = 0
    NetTotalAmount = 0
    temp = 0
    array = []
    difference = []
    unique_list = []
    for row in csvreader:
        i = i + 1
        if row[1] not in unique_list:
            unique_list.append(row[1])
    for x in unique_list: 
        print (x)
    print(f"Total number of votes: {i}")
    i = 0
    high = 0
    low = 0
    difference_total = 0
    for profit_loss in array:
        if i == 0:
            difference.append(0)
        else:
            difference.append(int(array[i] - array[i-1]))
        difference_total = difference_total + difference[i]
        i = i + 1
    print(f"Total number of months: {i}")
    print(f"Net Total Amount: {NetTotalAmount}")
    print(f"Profit/Loss Average change:{difference_total/(i-1)}")
    print(f"High:{max(difference)}")
    print(f"Low:{min(difference)}")