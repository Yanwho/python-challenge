import os
import csv

filepath = os.path.join("budget_data.csv")

sum_profits = (0)
month_count = (0)
monthly_change = []


# open the file and read it
with open("budget_data.csv", "r") as file:
    print("file: ", file)
    reader = csv.DictReader(file)
    print("reader: ", reader)
    print(10 * "=")
#  iterate through the file and perform calculations    
    for row in reader:
        month_count += 1
        row_dict = dict(row)
        profit = row_dict["Profit/Losses"]
        profit_float = float(profit) 
        sum_profits += profit_float
        
print(50 * "*")

# print the profit in a currency format with commas 2 decimal places
formatted_profit = "${:,.2f}".format(sum_profits)
print("Sum Profits: ", formatted_profit)
print("Month Count: ", month_count)