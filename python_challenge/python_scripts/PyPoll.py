#modules
import os
import sys
import csv

original_stdout = sys.stdout

#pathway
csvpath = os.path.join("..", "Resources", "election_data.csv")
output_path = os.path.join("..", "Resources", "election_analysis.csv")

#open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvfile)    

    rowcount = 0
    cand1 = 0
    cand2 = 0
    cand3 = 0
    cand4 = 0
    cands = []
    cands_uni = []
    cand_count = [0,0,0,0]
    win = cand_count[0]

    #count total votes and create list of individual votes
    for row in csvreader:
        rowcount += 1
        cands.append(row[2])

    for x in cands:
        #find unique candidate names
        if x not in cands_uni:
            cands_uni.append(x)

        #find candidate vote counts
        if x == cands_uni[0]:
            cand_count[0] += 1
        elif x == cands_uni[1]:
            cand_count[1] += 1
        elif x == cands_uni[2]:
            cand_count[2] += 1
        elif x == cands_uni[3]:
            cand_count[3] += 1
    
    #find greatest number of votes 
    for y in cand_count:
        if y > win:
            win = y

print("Election Results")
print("_________________________")
print(f"Total Votes: {rowcount} ")
print("_________________________")
for y in range(len(cands_uni)):
    print(f"{cands_uni[y]}: {round(cand_count[y]/rowcount*100, 2)}% ({cand_count[y]}) ")
print("_________________________")
print (f" Winner: {cands_uni[cand_count.index(win)]} ")
print("_________________________")

with open('PyPoll.txt','w') as f:
    sys.stdout = f
    print("Election Results")
    print("_________________________")
    print(f"Total Votes: {rowcount} ")
    print("_________________________")
    for y in range(len(cands_uni)):
        print(f"{cands_uni[y]}: {round(cand_count[y]/rowcount*100, 2)}% ({cand_count[y]}) ")
    print("_________________________")
    print (f" Winner: {cands_uni[cand_count.index(win)]} ")
    print("_________________________")
    sys.stdout = original_stdout

#with open(output_path, 'w', newline='') as csvfile:
#
#    csvwriter = csv.writer(csvfile, delimiter=',')
#
#    csvwriter.writerow(["Election Results"])
#    csvwriter.writerow([" "])
#    csvwriter.writerow(["Total Votes", rowcount])
#    csvwriter.writerow([" "])
#    csvwriter.writerow(["Candidate", "Votes(%)", "Votes(Count)"])
#    for y in range(len(cands_uni)):
#        csvwriter.writerow([cands_uni[y], round(cand_count[y]/rowcount*100, 2), cand_count[y]])
#    csvwriter.writerow([" "])
#    csvwriter.writerow(["Winner", cands_uni[cand_count.index(win)]])