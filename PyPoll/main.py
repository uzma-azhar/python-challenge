import os
import csv

csvPath = os.path.join("Resources", "election_data.csv")

with open (csvPath, "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")

    header = next(csvFile)
    totalVotes = 0
    votes = {} # empty dictionary to hold candidates and number of votes

    for row in csvReader:
        if row[2] in votes:
            votes[row[2]] = votes[row[2]] + 1 # adds candidates' names and tallies votes
        else:
            votes[row[2]] = 1
        
        totalVotes += 1 # calculates total votes cast

vPercent = [] # empty list for percentages 
for v in votes.values():
    vPercent.append((v/totalVotes)*100)

winner = max(votes, key=votes.get) # get key of max value
    
outputpath = os.path.join("Analysis", "analysis.txt")

with open (outputpath, "w") as textfile:
    textfile.write("Election Results")
    textfile.write(f"\n----------------------\n")
    textfile.write(f"Total Votes: {totalVotes}\n")
    textfile.write(f"\n----------------------\n")
    textfile.write(f"Charles Casper Stockham: {round(vPercent[0], 3)}% ({votes['Charles Casper Stockham']})\n")
    textfile.write(f"Diana DeGette: {round(vPercent[1], 3)}% ({votes['Diana DeGette']})\n")
    textfile.write(f"Raymon Anthony Doane: {round(vPercent[2], 3)}% ({votes['Raymon Anthony Doane']})\n")
    textfile.write(f"\n----------------------\n")
    textfile.write(f"Winner: {winner}")
    textfile.write(f"\n----------------------\n")

print("Election Results")
print(f"\n----------------------\n")
print(f"Total Votes: {totalVotes}\n")
print(f"\n----------------------\n")
print(f"Charles Casper Stockham: {round(vPercent[0], 3)}% ({votes['Charles Casper Stockham']})\n")
print(f"Diana DeGette: {round(vPercent[1], 3)}% ({votes['Diana DeGette']})\n")
print(f"Raymon Anthony Doane: {round(vPercent[2], 3)}% ({votes['Raymon Anthony Doane']})\n")
print(f"\n----------------------\n")
print(f"Winner: {winner}")
print(f"\n----------------------\n")


