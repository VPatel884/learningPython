# Problem 1
# Check wether word live is present in certificate.txt or not

file = open("Chapter8/certificate.txt", "r")
data = file.read().lower()

if "live" in data:
    print("Word is present in certificate.txt")
else:
    print("Word is not present in certificate.txt")

file.close()

# Problem 2
# Open a file called report.txt in write mode and add new data

reportFile = open("CHapter8/report.txt", "w")
reportFile.write("name : Vikash" 
"\nage : 28") # It will overwrite anything in the file

reportFile.close()

addDataInReport = open("Chapter8/report.txt", "a")
addDataInReport.write("\naddress : Bengaluru")

addDataInReport.close()

# Print number of lines in report.txt

with open("Chapter8/report.txt") as f:
    data = f.readlines()
    # print(data)
    print("Total number of lines in report is", len(data))

# Print each line in report.txt

with open("Chapter8/report.txt") as f:
    print("Line 1",f.readline())
    print("Line 2",f.readline())
    print("Line 3",f.readline())
    print("Line 4",f.readline())
    print(f.read()) # Prints empaty after all realines