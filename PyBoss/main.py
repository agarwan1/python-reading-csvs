import os
import csv

csvpath = os.path.join('File','employee_data1.csv')
csvpath2 = os.path.join('File','employee_data2.csv')

files = [csvpath, csvpath2]
ofile1 = "empdata1.csv"
ofile2 = "empdata2.csv"
ofile = [ofile1, ofile2]

#US states dictionary.
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

for csvpath in files:
    with open(csvpath, newline = '') as csvfile:
        output_file = os.path.join(ofile[files.index(csvpath)])
        with open(output_file,'w',newline='') as data_file:
            output_writer = csv.writer(data_file)
            output_writer.writerow(["Employee","First Name", "Last Name","DOB", "SSN", "State"])
            csvfile.readline()
            csvreader = csv.reader(csvfile, delimiter = ',')
			
#Format the name, date of birth, social security number and state.
            for row in csvreader:
                empid = row[0]
                parsename = row[1].split(" ")
                firstname = parsename[0]
                lastname = parsename[1]
				
#Format date to mm/dd/yyyy.
                parsedob = row[2].split("-")
                year = parsedob[0]
                month = parsedob[1]
                date = parsedob[2]
                dob = month + "/" + date + "/" + year
				
#Format social security number.
                parsessn = row[3].split("-")
                ssn = parsessn[2]
                ssn = "***-***" + ssn
				
#Format state.
                stateAbbrv = us_state_abbrev.get(row[4])
                state = stateAbbrv
				
#Print formatted csv.
                cleaned_csv = [empid, firstname, lastname, dob, ssn, state]
                print(cleaned_csv)
                output_writer.writerow(cleaned_csv)










