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
    voterID = []
    county = []
    candidate = []
    j = 0
    for row in csvreader:
        i = i + 1
        if row[1] not in unique_list:
            unique_list.append(row[1])
            #print(row[1])
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    print(voterID)
    print(county)
    print (candidate)
    #print(csvreader)
    # #for x in unique_list:
    #  #   y.append(0)
    #     for row in csvreader:
    #         print(row[1])
    #         if x == row[1]:
    #             y[j] = y[j] + int(row[2])
    #     j = j + 1
    # print(y)
    #for x in csvreader:
     #   i = i + 1 
      #  print(x[1])
        #if row[1] in unique_list:
          #  print(row[1][i])
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