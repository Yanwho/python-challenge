# import required modules
import os
import csv

# variable to point to data set
filepath = os.path.join("resources", "budget_data.csv")
# variable to point to new file being created
report_file = os.path.join("Analysis", "financial_analysis.txt")

# variables
best_gain = 0
worst_loss = 0
profit_difference = []
sum_profits = 0
month_count = 0
greatest_increase = float(-99999999999999)
greatest_decrease = float(999999999999)
best_month = 0
worst_month = 0

# create output file
output_file = "budget_analysis.txt"
# open the file and read it
with open(filepath, "r") as file:
    print("file: ", file)
    reader = csv.DictReader(file)

    print(10 * "=")

#  iterate through the file and perform calculations    
    for row in reader:
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
            # name the date associated with min and max
            if resulting_month == min(profit_difference):
                greatest_decrease = resulting_month
                worst_month = row["Date"]
            if resulting_month == max(profit_difference):
                greatest_increase = resulting_month
                best_month = row["Date"]

average_change = (sum(profit_difference) / len(profit_difference))
formatted_difference = "${:,.2f}".format(average_change)

formatted_profit = "${:,.2f}".format(sum_profits)
formatted_worst_loss = "${:,.2f}".format(worst_loss)
formatted_best_gain = "${:,.2f}".format(best_gain)
# # # printing of results for easy view in PyCharm without bouncing to and from file
# # print the profit and gains/losses in a currency format with commas 2 decimal places
# print(40 * "*")
# print("Sum Profits: ", formatted_profit)
# print("Month Count: ", month_count)
# print("Average Profit Difference: ", formatted_difference)
# # cannot get the best and worst month to print
# print("Best Month: ", (best_month))
# print("Best Gain: ", formatted_best_gain)
# print("Worst Month: ",worst_month)
# print("Worst Loss: ", formatted_worst_loss)
# print(40 * "*")
# writing the findings to the report file
with open(report_file, "w") as txt:
    txt.write("Financial Analysis:" + "\n")
    txt.write(40 * "-" + "\n")
    txt.write("Sum Profits: " + formatted_profit  + "\n")
    txt.write("Month Count: " + str(month_count)  + "\n")
    txt.write("Average Profit Difference: " + formatted_difference  + "\n")
    txt.write("Best Gain was "+ str(best_month) + " at: " + formatted_best_gain + "\n")
    txt.write("Worst Loss was " + str(worst_month) + " at: " + formatted_worst_loss  + "\n")
    txt.write(40 * "*")



