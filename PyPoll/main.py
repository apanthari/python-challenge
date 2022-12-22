
#load in packages
import csv
from statistics import mean
#find file location
election_csv = "../PyPoll/Resources/election_data.csv"


#open + read file
with open(election_csv, "r") as read:
    election_values = []
    csv_read = csv.reader(read, delimiter= ",") #what is this called? 
    for row in csv_read:
        election_values.append(row)   #total months


#removes the header
election_valuesjust = election_values[1:] #this doesnt work 

#total number of votes cast
all_values = len(election_valuesjust)



all_candidates = []
all_votes = []

#for total for each candidate got
charles = 0
diane = 0
raymond = 0

for i in range(len(election_valuesjust)): 
    all_candidates.append(election_valuesjust[i][2])

    all_votes.append(int(election_valuesjust[i][0]))

    if election_valuesjust[i][2] == "Charles Casper Stockham":
        charles += 1

    if election_valuesjust[i][2] == "Diana DeGette":
        diane += 1

    if election_valuesjust[i][2] == "Raymon Anthony Doane":
        raymond += 1


#loop through candidates so you find all unqiue candidates
unique_cand = [all_candidates[0]]
for candidate in range(1, len(all_candidates)): 
    if all_candidates[candidate] != all_candidates[candidate - 1] and all_candidates[candidate] not in unique_cand:
        unique_cand.append(all_candidates[candidate])

#get percentage each voter got 
charles_p = round(charles/all_values *100, 3)
diane_p = round(diane/all_values * 100, 3)
raymond_p = round(raymond/all_values * 100, 3)

#store in dictionary so winner can be found
winner = {unique_cand[0] : charles, unique_cand[1]: diane, unique_cand[2]: raymond}
winner_key = max(winner, key = winner.get)


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(all_values))
print("-------------------------")
print(unique_cand[0] + ": " + str(charles_p) + "%" + " (" + str(charles) + ")")
print(unique_cand[1] + ": " + str(diane_p) + "%" + " (" + str(diane) + ")")
print(unique_cand[2] + ": " + str(raymond_p) + "%" + " (" + str(raymond) + ")") 
print("-------------------------")
print("Winner: " + winner_key )
print("-------------------------")
