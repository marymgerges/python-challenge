# Modules
import os
import csv

# Set path for file
election_data_csv = os.path.join("Resources", "election_data.csv")

# Set initial variable for total number of votes cast
total_number_votes = 0

# Set initial index for the complete list of candidates who received votes
list_candidates_with_votes = {}

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:

     # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

     # Skip row of headers
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # Count the total number of votes cast
        total_number_votes += 1

        # Find all candidate names
        name_of_candidate = row[2]
        if name_of_candidate not in list_candidates_with_votes:
            list_candidates_with_votes[name_of_candidate] = 0

        # Add the votes cast for each candidate
        list_candidates_with_votes[name_of_candidate] += 1

# Print analysis to console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_number_votes}")
print("-------------------------")

# Set variable for the name of the winner
name_of_winner = ""

# Set initial number of votes for the winner
votes_for_winner = 0

# Calculate percentage of votes and total number of votes that each candidate won and print them
for name_of_candidate, votes in list_candidates_with_votes.items():
    percent = round(votes/total_number_votes*100, 3)
    print(f"{name_of_candidate}: {percent}% ({votes})")
    if votes > votes_for_winner:
        name_of_winner = name_of_candidate
        votes_for_winner = votes

# Print winner of the election based on popular vote
print("-------------------------")
print(f"Winner: {name_of_winner}")
print("-------------------------")

analysis = os.path.join("analysis/analysis_results.txt")

# Print analysis to text file
with open(analysis, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow("Election Results")
    csvwriter.writerow("----------------------------")
    csvwriter.writerow(f"Total Votes: {total_number_votes}")
    csvwriter.writerow("----------------------------")

    # Calculate percentage of votes and total number of votes that each candidate won and print them to text file
    for name_of_candidate, votes in list_candidates_with_votes.items():
        percent = round(votes/total_number_votes*100, 3)
        csvwriter.writerow(f"{name_of_candidate}: {percent}% ({votes})")
        if votes > votes_for_winner:
            name_of_winner = name_of_candidate
            votes_for_winner = votes

    csvwriter.writerow("----------------------------")
    csvwriter.writerow(f"Winner: {name_of_winner}")

# Print analysis to terminal
print(analysis)