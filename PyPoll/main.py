import csv
import os
from pathlib import Path
# Get the current script's directory
current_dir = Path(__file__).parent
# Construct the path to the CSV file
election_csv = current_dir / 'Resources' / 'election_data.csv'
pypoll_output = current_dir / 'analysis' / 'pypoll_output.txt'

# Initialize variables
Charles_total = 0
Diana_total = 0
Raymon_total = 0
total_votes = 0
try:
    with open(election_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # Skip the header row
        #The total number of votes each candidate won
        for row in csv_reader:
            total_votes += 1
            if row[2] == "Charles Casper Stockham":
                Charles_total += 1
            elif row[2] == "Diana DeGette":
                Diana_total += 1
            elif row[2] == "Raymon Anthony Doane":
                Raymon_total += 1

    #Calculate percentages
    Charles_percent = round((Charles_total/total_votes) *100, 3)
    Diana_percent = round ((Diana_total/total_votes) *100, 3)
    Raymon_percent = round((Raymon_total/total_votes) *100, 3)

    #The winner of the election based on popular vote
    if Charles_total > Diana_total and Charles_total > Raymon_total:
        winner = "Charles Casper Stockham"
    elif Diana_total > Raymon_total:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
        
    # Print results
    print ("Election Results")
    print ("--------------------------")
    print(f"Total Votes: {total_votes}")
    print ("--------------------------")
    print(f"Charles Casper Stockham: {Charles_percent}% ({Charles_total})")
    print(f"Diana DeGette: {Diana_percent}% ({Diana_total})")
    print(f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_total})")
    print ("--------------------------")
    print(f"Winner: {winner}")
    print ("--------------------------")

    # Save results to text file
    f = open(pypoll_output, "w")
    f.write ("Election Results\n")
    f.write ("--------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write ("--------------------------\n")
    f.write(f"Charles Casper Stockham: {Charles_percent}% ({Charles_total})\n")
    f.write(f"Diana DeGette: {Diana_percent}% ({Diana_total})\n")
    f.write(f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_total})\n")
    f.write ("--------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write ("--------------------------\n")
    f.close()

except FileNotFoundError:
    print(f"Error: The file {election_csv} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

