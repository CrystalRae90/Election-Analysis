#The data we need to retrieve 
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

candidate_options =[]
candidate_votes = {}

winning_candidate =""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

    #Print the header row 
    headers = next(file_reader)
  
  # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

     # Print the candidate name from each row.
        candidate_name = row[2]
    
        #Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name]=0

        candidate_votes[candidate_name] += 1

    
with open(file_to_save, "w") as txt_file:

    print(candidate_votes)

    for candidate_name in candidate_votes : 

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) *100     

       # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # winning_candidate_summary = (
    # f"-------------------------\n"
    # f"Winner: {winning_candidate}\n"
    # f"Winning Vote Count: {winning_count:,}\n"
    # f"Winning Percentage: {winning_percentage:.1f}%\n"
    # f"-------------------------\n")
    # print(winning_candidate_summary)

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")

    print(candidate_results)

    # Save the final vote count to the text file.
    txt_file.write(election_results)
