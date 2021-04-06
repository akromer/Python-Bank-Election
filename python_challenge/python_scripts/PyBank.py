#modules
import os
import sys
import csv

original_stdout = sys.stdout

#pathways
csvpath = os.path.join("..", "Resources", "budget_data.csv")
output_path = os.path.join("..", "Resources", "budget_analysis.txt")

#open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvfile)    

    rowcount = 0
    net = 0
    diff = []
    dates = []
    change = []

    for row in csvreader:
        rowcount += 1
        net += int(row[1])
        dates.append(row[0])
        diff.append(int(row[1]))

    for i in range(len(diff)-1):
        change.append(diff[i+1]-diff[i])

print (f"Total months: {rowcount} ")
print (f"Net change: {net} ")
print (f"Average change: {round((sum(change))/len(change), 2)} ")
print (f"Greatest Increase in Profits: {dates[(change.index((max(change))))+1]} ({max(change)})  ")
print (f"Greatest Decrease in Profits: {dates[(change.index((min(change))))+1]} ({min(change)})  ")


with open('PyBank.txt','w') as f:
    sys.stdout = f
    print (f"Total months: {rowcount} ")
    print (f"Net change: {net} ")
    print (f"Average change: {round((sum(change))/len(change), 2)} ")
    print (f"Greatest Increase in Profits: {dates[(change.index((max(change))))+1]} ({max(change)})  ")
    print (f"Greatest Decrease in Profits: {dates[(change.index((min(change))))+1]} ({min(change)})  ")
    sys.stdout = original_stdout

#with open(output_path, 'w', newline='') as csvfile:

#    csvwriter = csv.writer(csvfile, delimiter=',')

#    csvwriter.writerow(["Total months" , rowcount])
#    csvwriter.writerow(["Net change", net])
#    csvwriter.writerow(["Average change", round((sum(change))/len(change), 2)])
#    csvwriter.writerow(["Greatest Increase in Profits", dates[(change.index((max(change))))+1], (max(change)) ])
#    csvwriter.writerow(["Greatest Decrease in Profits", dates[(change.index((min(change))))+1], (min(change)) ])