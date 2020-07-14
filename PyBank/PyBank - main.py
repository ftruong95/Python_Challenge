# Import modules and dependencies
import os
import csv

# List variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set file path
csvpath = os.path.join('.', 'PyBank', 'Resources', 'python_budget_data.csv')

# Open csvfile
with open(csvpath) as csvfile:
    
     # CSV reader specifies delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate total amount, profit/loses
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read header row
    for row in csvreader:
        
        # Calculate total number of months
        total_months += 1
        # Calculate net amount of profit/loises
        net_amount += int(row[1])

        # Calculate change 
        change_in_revenue = int(row[1]) - previous_row
        monthly_change.append(change_in_revenue)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate greatest_increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate greatest_decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate average
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")