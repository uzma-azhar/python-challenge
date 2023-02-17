import os
import csv

# filepath
csvPath = os.path.join("Resources", "budget_data.csv")

with open(csvPath, "r") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    header = next(csvFile)
    months = 0 
    profitLosses = []
    netChanges = []
    oldProfitValue = 1088983 # first value 
    greatestIncrease = oldProfitValue # only change value we have so far therefore the greatest increase
    greatestDecrease = oldProfitValue # only change value we have so far therefore the greatest decrease

    for row in csvReader:
        profitLosses.append(float(row[1])) # list of all profits/losses
        totalAmount = sum(profitLosses)
        newChange = float(row[1])-float(oldProfitValue)

        if newChange > greatestIncrease: # stores new value & pulls date
            greatestIncrease = newChange
            greatestIncreaseDate = row[0]

        if newChange < greatestDecrease: # stores new value & pulls date
            greatestDecrease = newChange
            greatestDecreaseDate = row[0]

        netChanges.append(newChange) # list of changes in profits/losses
        oldProfitValue = row[1] # pulls new value
        months += 1
            
    averageChanges = sum(netChanges)/float(len(netChanges) -1) 

outputpath = os.path.join("Analysis", "analysis.txt")

with open (outputpath, "w") as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n-----------------------------\n")
    textfile.write(f"Total Months: {months}\n")
    textfile.write(f"Total: ${round(totalAmount)}\n")
    textfile.write(f"Average Change: ${round(averageChanges, 2)}\n")
    textfile.write(f"Greatest Increase in Profits: {greatestIncreaseDate} ({round(greatestIncrease)})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} ({round(greatestDecrease)})")

print("Financial Analysis")
print("\n-----------------------------\n")
print(f"Total Months: {months}\n")
print(f"Total: ${round(totalAmount)}\n")
print(f"Average Change: ${round(averageChanges, 2)}\n")
print(f"Greatest Increase in Profits: {greatestIncreaseDate} ({round(greatestIncrease)})\n")
print(f"Greatest Decrease in Profits: {greatestDecreaseDate} ({round(greatestDecrease)})")