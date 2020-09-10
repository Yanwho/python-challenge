import os
import csv

# naming varibles
candidate = []
vote_total = 0
candidates_count = {}
candidate_list = {}
filepath = os.path.join("resources", "election_data.csv")
report_file = os.path.join("Analysis", "election_results.txt")

# creating list of candidates from dataset
with open(filepath) as file:
    reader = csv.reader(file)
    next(reader)
    for row in csv.reader(file):
        vote_total += 1
        candidate.append(row[2])

# counting votes per candidate
candidates_count = [[count_of, candidate.count(count_of)] for count_of in set(candidate)]
candidates_count.sort()

# creating dictionary to identify winning vote getter by max element
for new in candidates_count:
    candidate_list[new[0]] = new[1:]
print(candidate_list)
print(type(candidate_list))
winner = max(candidate_list, key=candidate_list.get)

# prints to check code on the fly
print("Election Results")
print("-" * 25)
print("Total Votes: ", vote_total)
print("-" * 25)
print(winner + " is the winner!")

# isolating candidate vote count and calculating % of total vote
# would NOT work if i didnt know all of the candidates
candidate_0 = (candidates_count[0])
c = (candidate_0[0])
d = (candidate_0[1])
percent_won = round(((d) / vote_total) *100)
candidate_0_result = (f"{c}: {percent_won}% {d}")

candidate_1 = (candidates_count[1])
c = (candidate_1[0])
d = (candidate_1[1])
percent_won = round(((d) / vote_total) *100)
candidate_1_result = (f"{c}: {percent_won}% {d}")

candidate_2 = (candidates_count[2])
c = (candidate_2[0])
d = (candidate_2[1])
percent_won = round(((d) / vote_total) *100)
candidate_2_result = (f"{c}: {percent_won}% {d}")

candidate_3 = (candidates_count[3])
c = (candidate_3[0])
d = (candidate_3[1])
percent_won = round(((d) / vote_total) *100)
candidate_3_result = (f"{c}: {percent_won}% {d}")

# write resulting text file
with open(report_file, "w") as txt:
    txt.write("Election Results" + "\n")
    txt.write(25 * "-" + "\n")
    txt.write("Total Votes: " + str(vote_total) + "\n")
    txt.write(25 * "-" + "\n")
    txt.write(candidate_0_result + "\n")
    txt.write(candidate_1_result + "\n")
    txt.write(candidate_2_result + "\n")
    txt.write(candidate_3_result + "\n")
    txt.write(25 * "-" + "\n")
    txt.write("Winner: " + str(winner) + "\n")
    txt.write(25 * "-")