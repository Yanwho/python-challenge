import os
import csv
from typing import Iterator

path = os.path.join("..", "PyBank", "budget_data.csv")


with open(path, "r") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
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

