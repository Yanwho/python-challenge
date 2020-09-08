import os
import csv
from typing import List

filepath = os.path.join("budget_data.csv")
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


            # if float(profit_difference) > greatest_increase:
            #     greatest_increase = profit_difference
            #     best_month = row["Date"]

            # if float(row["Profit/Losses"]) > float(greatest_increase):
            #     greatest_increase = row["Date"]
            # if float(row["Profit/Losses"]) < float(greatest_decrease):
            #     greatest_decrease = row["Date"]





    average_change = (sum(profit_difference) / len(profit_difference))
    formatted_difference = "${:,.2f}".format(average_change)
    # Find best and worst months
    # if float(initial_month) < float(prior_month):
    #
    #
    # if float(resulting_month) < float(prior_month):
    #         greatest_increase = resulting_month





    # else:
    #     initial_month = row["Profit/Losses"]
    #     if float(resulting_month) > float(initial_month):
    #         greatest_decrease = prior_month
    #         worst_month = row["Date"]
    #         worst_loss = profit_difference




        # track the net change
        # net_change =
        # previous_net =
        # net_change_list += [net_change]
        # month_of_change += row["Date"]

        # calculate the greatest increase
        # calc the greatest decrease


        # net_change = 0
        # row_dict = dict(row)
        # profit = row_dict["Profit/Losses"]
        # profit_float = float(profit)
        # sum_profits += profit_float





print(50 * "*")

# print the profit in a currency format with commas 2 decimal places
formatted_profit = "${:,.2f}".format(sum_profits)
formatted_worst_loss = "${:,.2f}".format(worst_loss)
formatted_best_gain = "${:,.2f}".format(best_gain)
print("Sum Profits: ", formatted_profit)
print("Month Count: ", month_count)
print("Average Profit Difference: ", formatted_difference)
print("Best Month: ", best_month)
print("Best Gain: ", formatted_best_gain)
    # summary = f"Best Month: ", best_month, "Best Gain: ", best_gain"
print("Worst Month: ",worst_month)
print("Worst Loss: ", formatted_worst_loss)





