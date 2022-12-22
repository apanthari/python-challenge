#load in packages
import csv
from statistics import mean

#find file location
budget_csv = "../PyBank/Resources/budget_data.csv"
#open + read file
with open(budget_csv, "r") as read:
    csv_read = csv.reader(read, delimiter= ",") 
    budget_values = []
    for row in csv_read:
        budget_values.append(row) #store all rows in csv into a list 


    #removes the header
    budget_valuesjust = budget_values[1:]



    #total amount of months in the table
    total_months = len(budget_valuesjust)  

    #initiate lists 
    total_profit = []
    all_diff = []

    for month in range(len(budget_valuesjust)): #from 0 to 85 index
        total_profit.append(int(budget_valuesjust[month][1])) #append all month profits into list

        if month != len(budget_valuesjust)-1: #if it is NOT the last iteration
            #find all profits between months and add to list
            individual_diff = int(budget_valuesjust[month+1][1]) - int(budget_valuesjust[month][1])
            all_diff.append(individual_diff)


#find greatest/least profit values
greatest_value = max(all_diff)
index_greatest = all_diff.index(greatest_value)
greatest_value_date = budget_valuesjust[index_greatest+1][0]

lowest_value = min(all_diff)
index_lowest = all_diff.index(lowest_value)
lowest_value_date = budget_valuesjust[index_lowest+1][0]

#find total and avg profit
total_profit = sum(total_profit)
avg_diff = mean(all_diff)




print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(total_months))
print("Total: " + str(total_profit))
print("Average Change: " + "$" + str(round(avg_diff, 2)))
print("Greatest Increase in Profits: " + str(greatest_value_date) + " $" + str(greatest_value))
print("Greatest Decrease in Profits: " + str(lowest_value_date) + " $" + str(lowest_value))
