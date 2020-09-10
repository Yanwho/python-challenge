import os
import csv

candidate = []
vote_total = 0
candidates_count = {}

# print("candidates_count: ")
# print(type(candidates_count))

filepath = os.path.join("resources", "election_data.csv")
report_file = os.path.join("Analysis", "results.txt")

# Split the data on commas since that is your delimiter
with open(filepath) as file:
    reader = csv.reader(file)
    next(reader)
    for row in csv.reader(file):
        vote_total += 1
        candidate.append(row[2])



candidates_count = [[count_of, candidate.count(count_of)] for count_of in set(candidate)]

candidates_count.sort()
candidate_list = {}
# max_key = max(candidates_count, key=candidates_count.get)
# print(max_key)
for new in candidates_count:
    candidate_list[new[0]] = new[1:]
print(candidate_list)
print(type(candidate_list))
winner = max(candidate_list, key=candidate_list.get)


# zip(candidate_list)
# print(candidate_list)
# if int(candidates_count[0][1]) > int(candidates_count[1][1]):
#     winner = candidates_count[0]
# elif int(candidates_count[0][1]) > int(candidates_count[2][1]):
#     winner = candidates_count[0]
# elif int(candidates_count[0][1]) > int(candidates_count[3][1]):
#     winner = candidates_count[0]
# print(winner)

        # vote_total += 1
        # voter_id = row["Voter ID"]
        # county = row["County"]
        # candidate_name = row["Candidate"]

        # if candidate_name not in candidates:
        #     candidates.append(candidate_name)
        #     print(candidates)


        # candidates_count = candidates.count(candidate_name)
        #
        # print(candidates_count)

# print(candidate)
# print(candidates_count)
# print(candidates_count)

print("Election Results")
print("-" * 25)
print("Total Votes: ", vote_total)
print("-" * 25)

# print(candidates_count[0])
candidate_0 = (candidates_count[0])
c = (candidate_0[0])
d = (candidate_0[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")
candidate_0_result = (f"{c}: {percent_won}% {d}")

candidate_1 = (candidates_count[1])
c = (candidate_1[0])
d = (candidate_1[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")
candidate_1_result = (f"{c}: {percent_won}% {d}")


candidate_2 = (candidates_count[2])
c = (candidate_2[0])
d = (candidate_2[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")
candidate_2_result = (f"{c}: {percent_won}% {d}")


candidate_3 = (candidates_count[3])
c = (candidate_3[0])
d = (candidate_3[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")
candidate_3_result = (f"{c}: {percent_won}% {d}")

print(winner + " is the winner!")


with open(report_file, "w") as txt:
    txt.write("Election Results" + "\n")
    txt.write(40 * "-" + "\n")
    txt.write("Total Votes: " + str(vote_total) + "\n")
    txt.write(40 * "-" + "\n")
    txt.write(candidate_0_result + "\n")
    txt.write(candidate_1_result + "\n")
    txt.write(candidate_2_result + "\n")
    txt.write(candidate_3_result + "\n")
    txt.write("Winner: " + str(winner) + "\n")
    txt.write(40 * "*")


