import os
import re
import csv
csvpath = os.path.join('PyBankFile','budget_data_1.csv')
csvpath2 = os.path.join('PyBankFile','budget_data_2.csv')
files = [csvpath, csvpath2]
ofile1 = "budgetdata1.csv"
ofile2 = "budgetdata2.csv"
ofile = [ofile1, ofile2]

for csvpath in files:
    rowcnt = 0
    with open(csvpath, newline = '') as csvfile:
        output_file = os.path.join(ofile[files.index(csvpath)])
        with open(output_file,'w',newline='') as data_file:
            output_writer = csv.writer(data_file)
            output_writer.writerow(["Date","Revenue"])
            csvfile.readline() #equivalent to next
            csvreader = csv.reader(csvfile, delimiter = ',')
            #print(csvreader)
            #row = []

            totalrevenue = 0
            revenue = 0
            revenuechange = 0
            prevRev = 0
            maxrevchange = 0
            minrevchange = 0
            maxrevmonth = ""
            minrevmonth = ""
            for row in csvreader:
                month = row[0] #NEED TO COUNT
                revenue = row[1] #NEED TO SUM/AVERAGE
                rowcnt = rowcnt + 1 #This is the number of months.
                totalrevenue = float(totalrevenue) + float(row[1])
                revenuechange = int(revenue) - int(prevRev)
                prevRev = revenue
                if float(revenuechange) > float(maxrevchange):
                    maxrevchange = revenuechange
                    maxrevmonth = month
                if float(revenuechange) < float(minrevchange):
                    minrevchange = revenuechange
                    minrevmonth = month
            avgrevenue = totalrevenue / rowcnt
            avgrevchange = revenuechange / rowcnt
            print("Financial Analysis:" )
            print("Total Months:"+str(rowcnt))
            print(rowcnt)
            print("Total Revenue:" + str(totalrevenue))
            #print(totalrevenue)
            avgrevenue = totalrevenue / rowcnt
            print("Average Revenue:" + str(avgrevenue))
            #print(avgrevenue)
            print("Average Revenue Change" + str(avgrevchange))
            print("")
            print("Greatest Revenue Change: " + str(maxrevchange))
            print("Greatest Decrease Revenue Change: " + str(minrevchange))




