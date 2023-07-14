import os
import csv

# Navigating to the data file
csvpath = os.path.join('Resources', 'budget_data.csv')

#opens the data file so it can be read
with open(csvpath, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')

    #Skips past the header line
    csv_header = next(budget_data)

    # creates empty lists that can be used to cacluate what is needed in Financial Analysis
    months = []
    profits = []
    monthly_changes = []
    # Creates variables needed for calculations
    last_month = 0
    change_counter = 0

    
    for row in csvreader:
        
        #Adds each month to a list
        months.append(row[0])

        #Addes each Profit/Loss to a list, and sets it as an integer
        profits.append(int(row[1]))

        #sets a variable needed to calculate montly change in Profit/Loss
        this_month = int(row[1])
        
        #Conditional to account for no change in the first month
        if change_counter == 0:
            last_month = int(row[1])
            change_counter += 1            
        #Calculates monthly change and adds to list. Sets new value for last_month, 
        # and advances the change counter
        else:
            monthly_change = (this_month - last_month)
            monthly_changes.append(monthly_change)
            last_month = int(row[1])
            change_counter += 1

#Calculate and set value for greatest increase and decrease
greatest_increase = max(monthly_changes)
greatest_decrease = min(monthly_changes)

#Loops through the file again to find the date of the greatest in/decrease
with open(csvpath, 'r') as budget_data:
    
    csvreader = csv.reader(budget_data, delimiter=',')
    
    csv_header = next(budget_data)

    last_month = 0
    change_counter = 0

    for row in csvreader:
        this_month = int(row[1])
        
        if change_counter == 0:
            last_month = int(row[1])
            change_counter += 1            
        else:
            monthly_change = (this_month - last_month)
            last_month = int(row[1])
            change_counter += 1

            # finds the dates of greatest in/decrease and sets it to a variable
            if monthly_change == greatest_increase:
                gi_date = row[0]
            elif monthly_change == greatest_decrease:
                gd_date = row[0]

    #Calculates and sets the data points needed for the Analysis
    total_months = len(months)
    total_profits = sum(profits)
    average_change = round((sum(monthly_changes) / (change_counter - 1)),2)

#prints Financial Analysis in terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_profits}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {gi_date} (${greatest_increase})') 
    print(f'Greatest Decrease in Profits: {gd_date} (${greatest_decrease})') 

#Writes Financial Analysis to text file in analysis folder
output_path = os.path.join('analysis', 'Financial_Analysis.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${total_profits}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {gi_date} (${str(greatest_increase)})\n') 
    txtfile.write(f'Greatest Decrease in Profits: {gd_date} (${str(greatest_decrease)})\n') 