import os
import csv




khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

candidates = []

filepath = os.path.join("resources", "election_data.csv")

# Split the data on commas since that is your delimiter
with open(filepath) as file:
    for row in csv.DictReader(file):
        voter_id = row["Voter ID"]
        county = row["County"]
        candidate = row["Candidate"]
        if candidate not in candidates:
            candidates.append(candidate)
    for candidate in candidates:
        if candidate == "Khan":
            khan_count += 1
        elif candidate == "Correy":
                correy_count += 1
        elif candidate == "Li":
                li_count += 1
        elif candidate == "O'Tooley":
                otooley_count += 1
    print(khan_count)
    print(correy_count)
    print(li_count)
    print(otooley_count)
    print(candidates)



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