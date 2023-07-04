import os
import csv

Names_ = []

# Path to collect data from the Resources folder
PyPollCSVPath = os.path.join("Resources/election_data.csv")
with open(PyPollCSVPath) as PyPollCSVFile:
    PyPollFile = csv.reader(PyPollCSVFile)
    header = next(PyPollFile) 
    list_File = list(PyPollFile)
    List_Lenght = len(list_File)

# Print in Terminal 
print("Election Results")
print("-------------------------")
print("Total Votes:" + str(List_Lenght))

# Print Text file
# + ".\n" adds a line break
file_output = os.path.join("Text_Output.txt")
with open(file_output,"w") as f:
    f.write(str("Election Results") + ".\n")
    f.write(str("----------------------------")+ ".\n")
    f.write(str("Total Votes:") + str(List_Lenght)+ ".\n")