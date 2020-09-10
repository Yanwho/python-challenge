import os
import csv

candidate = []
vote_total = 0
candidates_count = [0]
# print("candidates_count: ")
# print(type(candidates_count))

filepath = os.path.join("resources", "election_data.csv")

# Split the data on commas since that is your delimiter
with open(filepath) as file:
    reader = csv.reader(file)
    next(reader)
    for row in csv.reader(file):
        vote_total += 1
        candidate.append(row[2])

candidates_count = [[count_of, candidate.count(count_of)] for count_of in set(candidate)]


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

candidate_1 = (candidates_count[1])
c = (candidate_1[0])
d = (candidate_1[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")

candidate_2 = (candidates_count[2])
c = (candidate_2[0])
d = (candidate_2[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")

candidate_3 = (candidates_count[3])
c = (candidate_3[0])
d = (candidate_3[1])
percent_won = round(((d) / vote_total) *100)
print(f"{c}: {percent_won}% {d}")




    #         if candidate == "Khan":
    #             khan_count += 1
    #         elif candidate == "Correy":
    #             correy_count += 1
    #         elif candidate == "Li":
    #             li_count += 1
    #         elif candidate == "O'Tooley":
    #             otooley_count += 1
    # print(khan_count)
    # print(correy_count)
    # print(li_count)
    # print(otooley_count)
    # print(candidates)

    # khan_count = 0
# correy_count = 0
# li_count = 0
# otooley_count = 0


    # csvreader = csv.reader(file, delimiter=',')
    # line = next(csvreader, None)
    # for row in file:
        # ballot = row.split(",")
        # candidate = (ballot[2])
        # voter_id = (ballot[0])
        # county = (ballot[1])
        # candict = dict(zip(candidate))
        # print(candict)
        # candidate = (voter_id[2])
        # candidates.append(row)
        # print(voter_id)

        # row = dict(row)
        # total_votes = int(row["total_votes_cast"])
        # candidate_tally = int(row["Candidate_votes"]
        # ["Percent_won"] = row["total_votes_cast"] / row["Candidate_votes"]
        #
        # csv_writer.writerow(row)

        # ["Voter ID",
        #  "County",
        #  "Candidate"
        #  "total_votes_cast",
        #  "list_of_candidates",
        #  "Candidate_votes",
        #  "Percent_won"])




    # The total number of votes cast
#
# A complete list of candidates who received votes
#
# The percentage of votes each candidate won
#
# The total number of votes each candidate won
#
# The winner of the election based on popular vote.