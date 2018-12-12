# 03 - Python Homework
#  PyBank

# import modules 
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# open file and set to read w/ commas separatein
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

print(csv_reader)



