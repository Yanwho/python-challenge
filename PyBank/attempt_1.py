import os
import csv
from typing import Iterator

path = os.path.join("..", "PyBank", "budget_data.csv")


with open(path, "r") as file:
    # reader = csv.reader(file)
    reader = csv.reader(file)
    for row in reader:
        print(row)





    # header = file.readline()
    # print("this is the header.")
    # print(header)


    data = file.readlines()
    # print("This is the data.")


    for row in data:
        print(row.strip().split(","))
# print([row.strip().split(",") for row in data])

# Determines and prints the number of months in the report
    row_count = len(row)
    print(f"This report contains {row_count} months")

print("""**********
**********
**********
**********""")

# Second attempt at math to column

# csv_reader = csv.DictReader(file)
# data_1 = list(csv.reader)

# OUT_PATH = 'augmented_PyBank.csv'
# with open(path, "r") as file:
#     csv_writer = csv.DictWriter(file,
#                                 ["Date",
#                                  "profit"])
#
#     csv_writer.writeheader()
#     for row in data_1:
#         row = dict(row)
#
#         profit = int(row[profit])
#     sum_of_profit = sum(profit)
#     print(profit)



   # with open(OUT_PATH, "w+") as file:



path = os.path.join("..", "PyBank", "budget_data.csv")

with open("budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)
        break
    next(csv_reader)
    print(row)


        # value = (type(row[1]))
        # int_value = int(value)
        # print(value)


        # print(integer)


        # profitstr = (row[1])
        # profitint = int(profitstr)
        # print(sum(profit_int))