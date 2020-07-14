# Import modules and dependencies
import os
import csv

# List variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set file path
csvpath = os.path.join('.', 'PyPoll', 'Resources', 'python_election_data.csv')

# Open csvfile
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read header row
    csv_header = next(csvfile)
    for row in csvreader:
        
        # Calculate number of votes casted
        total_votes += 1
        
        # Calculate total number of votes
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    # Calculate percentage of votes
    percentage_for_khan = khan_votes / total_votes
    percentage_for_correy = correy_votes / total_votes
    percentage_for_li = li_votes / total_votes
    percentage_for_otooley = otooley_votes / total_votes
    
    # Calculate winner
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

# Print final results
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {percentage_for_khan:.3%}({khan_votes})")
print(f"Correy: {percentage_for_correy:.3%}({correy_votes})")
print(f"Li: {percentage_for_li:.3%}({li_votes})")
print(f"O'Tooley: {percentage_for_otooley:.3%}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")