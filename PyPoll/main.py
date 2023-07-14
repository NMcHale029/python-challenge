import os
import csv
import statistics


# Navigating to the data file
csvpath = os.path.join('Resources', 'election_data.csv')

#opens the data file so it can be read
with open(csvpath, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    #Skips past the header line
    csv_header = next(csvreader)

    #Variables needed for calculations
    vote_count = 0
    candidate_list = []

    #Tallies the vote count, and creates a list of each vote
    for row in csvreader:
        vote_count += 1
        candidate_list.append(row[2])

    #Creates a list of unique candidates from the data set
    candidates = sorted(set(candidate_list))

print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {vote_count}\n")
print("-------------------------\n")

#Loops through the list of unique candidates
for candidate in candidates:
    
    #Generates a count of occurances of the candidate in the list of all votes
    vote_tally = candidate_list.count(candidate)

    #Calculates the percentage of vote the candidate recieved
    vote_percentage = round((vote_tally / vote_count)*100,3)

    #Prints result for each candidate    
    print(f"{candidate.title()}: {vote_percentage}% ({vote_tally})\n")

print("-------------------------\n")
print(f"Winner: {statistics.mode(candidate_list)}\n")
print("-------------------------")

#Writes election results to text file in analysis folder
output_path = os.path.join('analysis', 'election_results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {vote_count}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        vote_tally = candidate_list.count(candidate)
        txtfile.write(f"{candidate.title()}: {round((vote_tally / vote_count)*100,3)}% ({vote_tally})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {statistics.mode(candidate_list)}\n")
    txtfile.write("-------------------------") 
