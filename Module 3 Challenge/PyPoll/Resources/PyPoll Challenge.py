import csv
import pandas as pd

#Define the file path
file_path = ("PyPoll/Resources/election_data.csv")
df = pd.read_csv(file_path)

#Find the Total Number of Votes Cast
vote_count = df["Ballot ID"].count()

#List the candidates who received votes
Candidate_Vote_Count = df.groupby("Candidate").count()["Ballot ID"]

#Calculate the percentage of votes for each candidate
Vote_Per = (Candidate_Vote_Count/vote_count) * 100

#Winner based on popular vote
winner = Candidate_Vote_Count.idxmax()

# Print out the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for candidate, votes in Candidate_Vote_Count.items():
    print(f"{candidate}: {Vote_Per[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

