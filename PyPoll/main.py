#   03 - Python Homework
#   PyPoll

#   import modules 
import os
import csv

#   declare a list to hold voter ID, County and Canidate data
voterID = []
counties = []
canidates = []

csvpath = os.path.join('Resources', 'election_data.csv')

#   open file and set to read w/ commas separatein
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
#   show file opject to be read
    print(csvreader)


    #   populate the months list with data from 1st column (skip header)
    #   find length of months list
    for row in csvreader:
        
        voterID.append(row[0])
        length = len(voterID)
    print(length)
#   open file and set to read w/ commas separatein
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
    #   show file opject to be read
    print(csvreader)

    #   define a function to return a list with unique items from another list
    def unique(list1): 
        # intilize a null list 
        unique_list = [] 
        # traverse for all elements 
        for x in list1: 
            # check if exists in unique_list or not 
            if x not in unique_list: 
                unique_list.append(x) 
        # print list 
        return unique_list,
             
    
    #   populate the canidate list with 3rd column of csv file
    for row in csvreader:
        canidates.append(row[2])
    #   use unique() functions to return a list of unique canidate names
    canidates = unique(canidates)
    print(canidates)
      
    #for x in canidate:








#   Print out report
print("Election Results")
print("****************************************")        
print("Total Votes: ", str(length))
print("****************************************")
print()



    