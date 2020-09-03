import os
import csv


path = os.path.join("..", "PyBank", "budget_data.csv")
total_revenue = 0 

with open(path, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    header = csvfile.readline()
    print("this is the header.")
    print(header)


    data = csvfile.readlines()
    print("This is the data.")
    for row in data:
        all_data = (row.strip().split(","))
        print(all_data)
        
    month_count = len(data)
    print(month_count)
    
    return sum(data[1])

sum = 0
for row in dict_reader:
	sum += float(row["Profit/Loss"])

# *************************************************************   

# total = sum(int(x) for x in columns[1])
     
#         csv_reader = csv.DictReader(csv_file)
#         for line in csv_reader:
#         column =(line["Profit/Losses"])
#         column_int = int(column)
        
    
#     headerline = csv_file.next()
#     total = 0
#     for row in csv.reader(csv_file):
#         total += int(row[1])
#     print total
        
        
# #         print(column_int)
# #         print(line["Profit/Losses"])
# #         print(sum(["Profit/Losses"]))