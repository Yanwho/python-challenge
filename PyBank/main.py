import os
import csv
from typing import List

filepath = os.path.join("budget_data.csv")
OUT_PATH = os.path.join("Analysis", "financial_analysis.txt")

prior_month = 0

best_month = 0
best_gain = 0
worst_month = 0
worst_loss = 0

sum_month = 0
profit_difference = []
initial_month = 0
sum_profits = 0
month_count = 0
monthly_change = []
net_change_list = []
greatest_increase = float(-99999999999999)
greatest_decrease = float(999999999999)

# The total number of months included in the dataset
#
# The net total amount of "Profit/Losses" over the entire period
#
# The average of the changes in "Profit/Losses" over the entire period
#
# The greatest increase in profits (date and amount) over the entire period
#
# The greatest decrease in losses (date and amount) over the entire period


# create output file
output_file = "budget_analysis.txt"
# open the file and read it
with open("budget_data.csv", "r") as file:
    print("file: ", file)
    reader = csv.DictReader(file)




    # print("reader: ", reader)
    print(10 * "=")


#  iterate through the file and perform calculations    
    for row in reader:

        # track the month count

        # track the total
        # sum_profits += int(row[1])
        month_count += 1
        sum_profits += float(row["Profit/Losses"])
        if month_count == 1:
            prior_month = row["Profit/Losses"]
        else:
            resulting_month = float(row["Profit/Losses"]) - float(prior_month)
            profit_difference.append(resulting_month)
            prior_month = row["Profit/Losses"]
            worst_loss = min(profit_difference)
            best_gain = max(profit_difference)

    average_change = (sum(profit_difference) / len(profit_difference))
    formatted_difference = "${:,.2f}".format(average_change)

print(40 * "*")

# print the profit and gains/losses in a currency format with commas 2 decimal places
formatted_profit = "${:,.2f}".format(sum_profits)
formatted_worst_loss = "${:,.2f}".format(worst_loss)
formatted_best_gain = "${:,.2f}".format(best_gain)
print("Sum Profits: ", formatted_profit)
print("Month Count: ", month_count)
print("Average Profit Difference: ", formatted_difference)
# cannot get the best and worst month to print
print("Best Month: ", best_month)
print("Best Gain: ", formatted_best_gain)
print("Worst Month: ",worst_month)
print("Worst Loss: ", formatted_worst_loss)
print(40 * "*")
# writing the findings to the report file
with open(OUT_PATH, "w") as txt:
    txt.write("Financial Analysis:" + "\n")
    txt.write(40 * "-" + "\n")
    txt.write("Sum Profits: " + formatted_profit  + "\n")
    txt.write("Month Count: " + str(month_count)  + "\n")
    txt.write("Average Profit Difference: " + formatted_difference  + "\n")
    # cannot get the month to print
    txt.write("Best Month: " + str(best_month)  + "\n")
    txt.write("Best Gain: "+ formatted_best_gain + "\n")
    txt.write("Worst Month: " + str(worst_month) + "\n")
    txt.write("Worst Loss: " + formatted_worst_loss  + "\n")
    txt.write(40 * "*")



