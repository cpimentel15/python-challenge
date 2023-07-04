import os
import csv

Total_ = 0
Total_Months = 0
Total_Changes = 0
Previous_PL = 0
Max_Increase = 0
Max_Month = ""
Min_ = 0
Min_Month = ""

PybankCSVPath = os.path.join("Resources/budget_data.csv")
with open(PybankCSVPath) as PybankCSVFile:
    PybankFile = csv.reader(PybankCSVFile)

    Header = next(PybankFile)

    for row in PybankFile:
        current = int(row[1])
        Total_Months = Total_Months + 1
        Total_ = Total_ + current
        
        if Total_Months > 1: 
            change_PL = current - Previous_PL
            Total_Changes = Total_Changes + change_PL
            if change_PL > Max_Increase:
                Max_Increase = change_PL
                Max_Month = row[0]
            if change_PL < Min_:
                Min_ = change_PL
                Min_Month = row[0]

        Previous_PL = current  


print(" Financial Analysis")
print("----------------------------")
print("Total Months:", Total_Months)
print("Total:", Total_)
print("Average Change:", Total_Changes/(Total_Months-1))
print("Greatest Increase in Profits:", Max_Increase, Max_Month)
print("Greatest Decrease in Profits:", Min_, Min_Month) 

file_output = os.path.join("Text_Output.txt")
with open(file_output,"w") as f:
    f.write(str("Financial Analysis") + ".\n")
    f.write(str("----------------------------")+ ".\n")
    f.write(str("Total Months:") + str(Total_Months)+ ".\n")
    f.write(str("Total:") + str(Total_)+ ".\n")
    f.write(str("Average Change:") + str(Total_Changes/(Total_Months-1))+ ".\n")
    f.write(str("Greatest Increase in Profits:") + str(Max_Increase) + "  " + str(Max_Month)+ ".\n")
    f.write(str("Greatest Decrease in Profits:") + str(Min_) + "  " + str(Min_Month) + ".\n") 
    f.close()