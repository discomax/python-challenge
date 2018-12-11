#   03 - Python Homework
#   PyBank

#   import modules 
import os
import csv

#   list used to store data
months = []
profit_losses = []
profit_var = []
#   placeholder to keep tally of profit while performing arithmetic
profit_tally = 0

csvpath = os.path.join('Resources', 'budget_data.csv')

#   open file and set to read w/ commas separatein
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
#   show file opject to be read
    print(csvreader)

    #   populate the months list with data from 1st column (skip header)
    #   find length of months list
    for row in csvreader:
        
        months.append(row[0])
        length = len(months)

    #print("Total Months: " + str(length))

#   Find the total profit
    
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    #   populate the profit/losses list with column 2 data (skip header)    
    for row in csvreader:
        profit_losses.append(int(row[1]))
    
    #   add the numbers in the list w/ the sum function
    profit_tally = (sum(profit_losses))
    
    #create list of the diffferences between values in profit/losses list
    def argmax(iterable):
        return max(enumerate(iterable), key=lambda x: x[1])[0]

    profit_var = [profit_losses[i+1]-profit_losses[i]
        for i in range(len(profit_losses)-1)]
  
    #   calculate the average of the list of differences
    #   and assign to new variable: avg_profit_var.
    avg_profit_var = round(sum(profit_var) / len(profit_var), 2)
    

    #   find the greatest increase in profits (date and amount) over the entire period
    #   and assign to variable: max_profit_var.
    max_profit_var = max(profit_var)
    
    #   find the greatest decrease in profits (date and amount) over the entire period
    #   and assign to variable: min_profit_var.
    min_profit_var = min(profit_var)

    
#   Print out report
print("Financial Analysis")
print("****************************************")        
print("Total Months: " + str(length))
print("Total Profit: $", str(profit_tally))   
print("Average Change: $", str(avg_profit_var))
print("Largest Increase in Profits: $", str(max_profit_var))
print("Largest Decrease in Profits: $", str(min_profit_var))

# Specify the file to write to
output_path = os.path.join("output", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("****************************************")        
    txtfile.write("Total Months: " + str(length))
    txtfile.write("Total Profit: $" + str(profit_tally))   
    txtfile.write("Average Change: $" + str(avg_profit_var))
    txtfile.write("Largest Increase in Profits: $" + str(max_profit_var))
    txtfile.write("Largest Decrease in Profits: $" + str(min_profit_var))






