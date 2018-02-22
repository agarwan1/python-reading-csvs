import os
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
            output_writer.writerow(["Total Months", "Total Revenue", "Average Revenue Change", "Greatest Revenue Change","Greatest Decrease Revenue Change"])
            csvfile.readline() #equivalent to next
            csvreader = csv.reader(csvfile, delimiter = ',')
            #print(csvreader)
            #row = []

#Initializing all variabes.
            totalrevenue = 0
            totalRevenueChange = 0
            revenue = 0
            rowcnt = 0
            revenuechange = 0
            prevRev = 0
            maxrevchange = 0
            minrevchange = 0
            maxrevmonth = ""
            minrevmonth = ""
            avgrevenue = 0
            avgrevchange = 0
#Looping through rows.
            for row in csvreader:
                month = row[0]
                revenue = row[1]
                rowcnt = rowcnt + 1 #This is the number of months.
                totalrevenue = float(totalrevenue) + float(row[1])
#I don't want to include the first row with the data. Revenue change needs to start from second month.
                if rowcnt > 1:
                    revenuechange = int(revenue) - int(prevRev)
                    totalRevenueChange = totalRevenueChange + revenuechange
#I don't want to skip the first row of data for the previous revenue.
                prevRev = revenue
#Compare this row's revenue change against the maximum revchange. Only keep maximum revenue change.
                if float(revenuechange) > float(maxrevchange):
                    maxrevchange = revenuechange
                    maxrevmonth = month
#Compare this row's revenue change against the minimum revchange. Only keep minimum revenue change.
                if float(revenuechange) < float(minrevchange):
                    minrevchange = revenuechange
                    minrevmonth = month
#Calculate average revenue and average revenue change.
            avgrevenue = totalrevenue / rowcnt - 1
            avgrevchange = round((totalRevenueChange / (rowcnt - 1)), 2)
#Print the results.
            print("Financial Analysis:" )
            print("----------------------------")
            print("Total Months: "+str(rowcnt))
            #print(rowcnt)
            print("Total Revenue: " + str(totalrevenue))
            #print(totalrevenue)
            #avgrevenue = totalrevenue / rowcnt
            #print("Average Revenue: " + str(avgrevenue))
            print("Average Revenue Change: " + str(avgrevchange))
            print("Greatest Revenue Change: " + str(maxrevchange))
            print("Greatest Decrease Revenue Change: " + str(minrevchange))
            print("")

            listtwo = [rowcnt, totalrevenue, avgrevchange, maxrevchange, minrevchange]
            print(listtwo)
            output_writer.writerow(listtwo)

