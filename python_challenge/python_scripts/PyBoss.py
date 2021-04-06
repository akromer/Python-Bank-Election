#modules
import os
import csv

#pathway
csvpath = os.path.join("..", "Resources", "employee_data.csv")
output_path = os.path.join("..", "Resources", "employee_analysis.csv")

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    csv_header = next(csvfile)

    eid = []
    name = []
    dob = []
    ssn = []
    state = []

    first = []
    last = []
    ssn_new = []
    state_new = []

    #parse lists
    for row in csvreader:
        eid.append(row[0])
        name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])
    
    #split first and last names
    for i in name:
        first.append(i.split(" ",1)[0])
        last.append(i.rsplit(" ",1)[1])

    #split last four of ssn and combine with redacted numbers
    for j in ssn:
        ssn_new.append(j.split("-",2)[2])
    ssn_hid = [("XXX-XX-" + num) for num in ssn_new]
    
    #look up state and create new list using abbreviations
    for k in state:
        state_new.append(us_state_abbrev[k])

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["EID", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    for l in range(len(eid)):
        csvwriter.writerow([eid[l], first[l], last[l], dob[l], ssn_hid[l], state_new[l]])