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
    for row in csvreader:
        i = i + 1
        if row[2] not in unique_list:
            unique_list.append(row[2])
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    print(f"Total number of votes: {i}")
    print(unique_list)
    voterCount = []
    j = 0
    for x in unique_list:
        voterCount.append(0)
        for y in candidate:
            if x == y:
                voterCount[j] = voterCount[j] + 1
        j = j + 1
    print(voterCount)
    for x in voterCount:
        print(f"{round((x/i)* 100)}%", end=" ")
    print(f"")
    win_position = voterCount.index(max(voterCount)) 
    print(f"Winner is: {candidate[win_position]}")