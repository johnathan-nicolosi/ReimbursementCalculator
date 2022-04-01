import datetime
from collections import Counter

### Reimbursement rates ###
# Low Cost Cities
lcc_td = 45
lcc_fd = 75
# High Cost Cities
hcc_td = 55
hcc_fd = 85

# number of projects in low cost cities
lccTotal = 0
# number of projects in high cost cities
hccTotal = 0

### Calculate Rates ###
# Default settings
numberDays = 0
numberTravelDays = 0
numberFullDays = 0
# Calculations
reimbursement_lcc_td = numberTravelDays * lcc_td
reimbursement_lcc_fd = numberFullDays * lcc_fd
reimbursement_hcc_td = numberTravelDays * hcc_td
reimbursement_hcc_fd = numberFullDays * hcc_fd

# empty lists for start and stop dates
startDates = []
endDates = []

# Get number of projects from user
while True:
    numProjects = input("Enter number of projects: ")
    try:
        numProjects = int(numProjects)
    except:
        print("please enter a numerical value")
        continue
    if numProjects < 1:
        print("Please enter value greater than 0")
        continue
    break

print("Number of projects for this set = ", numProjects)
numberProjects = int(numProjects)

# for each project enter the type of city, start date and end date
while numberProjects > 0:
    for i in range(numberProjects):
        print("")
        print("Project ", str(i + 1))

        # get type of city from user
        typeCity = input("Enter lcc for low cost city or hcc for high cost city: ")
        while typeCity != "LCC" and typeCity != "lcc" and typeCity != "HCC" and typeCity != "hcc":
            typeCity = input("Please enter lcc or hcc : ")

       # convert user input to uppercase
        typeCity = typeCity.upper()

        # counts the number of LCCs and HCCs for each set of projects
        if typeCity == "LCC":
            lccTotal = lccTotal + 1
        elif typeCity == "HCC":
            hccTotal = hccTotal + 1

        # get start date from user
        startDay = str(input("Enter start date of project (in MM/DD/YYYY): "))
        startDate = datetime.datetime.strptime(startDay, "%m/%d/%Y").date()

        # Add start date to list

        startDates.append(startDay)

        # get end date from user
        endDay = str(input("Enter end date of project (in MM/DD/YYYY): "))
        endDate = datetime.datetime.strptime(endDay, "%m/%d/%Y").date()

        # Add end date to list

        endDates.append(endDay)

        # calculate number of days for project
        if endDate == startDate:
            numDays = 1
            numTravelDays = 1
            numFullDays = 0
        else:
            numDays = (endDate - startDate)
            numDays = int(numDays.days + 1)
            numTravelDays = 2
            numFullDays = int(numDays - numTravelDays)

        numberDays = numberDays + numDays
        numberTravelDays = numberTravelDays + numTravelDays
        numberFullDays = numberFullDays + numFullDays

        numberProjects -= 1

numberUniqueStartDates = Counter(startDates).keys()
numberUniqueEndDates = Counter(endDates).keys()

print("\nTotal number of Days = ", str(numberDays))
print("Number of Travel Days = ", str(numberTravelDays))
print("Number of Full Days = ", str(numberFullDays))
print("")
print("Number of LCCs = ", str(lccTotal))
print("Number of HCCs = ", str(hccTotal))
print("")
print("Start Dates")
print(startDates)
print("Number of unique start dates = ", len(numberUniqueStartDates))

print("\nEnd Dates")
print(endDates)
print("Number of unique end dates = ", len(numberUniqueEndDates))


