############################################################
#                                                          #
#                  Reimbursement Calulator                 #
#              Written by: Johnathan Nicolosi              #
#                                                          #
############################################################

import json
import datetime
from collections import Counter

### Employees ###
# list of employees
listEmployees = []
# number of employees 
numEmployees = 0

### Reimbursement rates ###
###########################
#     Low Cost Cities     #
###########################
# travel day reimbursement rate for LCC
lcc_td_rr = 45
# full day reimbursement rate for LCC
lcc_fd_rr = 75
# number of projects in low cost cities
lccTotalDays = 0
###########################
#    High Cost Cities     #
###########################
# travel day reimbursement rate for HCC
hcc_td_rr = 55
# full day reimbursement rate for HCC
hcc_fd_rr = 85
# number of projects in high cost cities
hccTotalDays = 0

###########################
#      Date Variables     #
###########################
# number of days  
num_days = 0
# travel days
numTravelDays = 0
numTravelDaysLCC = 0
numTravelDaysHCC = 0
# full days
numFullDays = 0
numFullDaysLCC = 0
numFullDaysHCC = 0

###########################
#   Start and End Dates   #
###########################
# lists of start and stop dates
startDates = []
endDates = []
# start dates
lccStartDates = []
hccStartDates = []
# end dates
lccEndDates = []
hccEndDates = []


# Open JSON file
fileName = input("Enter name of file you would like to read (.json files only): ")
with open(fileName) as file:

    data = json.load(file)
    dumped = json.dumps(data)

    # print the json file
    # print(json.dumps(data, indent=2))
    print()

    print("\nPrinting nested dictionary as key-value pair\n")
    for i in data["projects"]:
        startDates.append(i["startDate"])
        start_date = datetime.datetime.strptime(i["startDate"], "%m/%d/%Y").date()
        endDates.append(i["endDate"])
        end_date = datetime.datetime.strptime(i["endDate"], "%m/%d/%Y").date()

        if i["name"] not in listEmployees:
            listEmployees.append(i["name"])
            numEmployees = numEmployees + 1

        if i["cityType"] == 'LCC':
            # print(f'Project: {i["cityType"]} City')
            # print("Name: ", i['name'])
            # print("Start Date: ", i['startDate'])
            # print("End Date: ", i['endDate'])
            # print("City Type: ", i['cityType'])
            lccStartDates.append(i['startDate'])
            lccEndDates.append(i['endDate'])

            if start_date == end_date:
                numDays = 1
                numTravelDays = 1
                numFullDays = 0
                print("LCC travel Day")
            else:
                numDays = end_date - start_date
                numDays = int(numDays.days + 1)
                numTravelDays = 2
                numFullDays = numDays - numTravelDays
                if numFullDays < 0:
                    numFullDays = 0
                #print(numDays)
                # print(numFullDays)

            numFullDaysLCC = numFullDaysLCC + numFullDays
            numTravelDaysLCC = numTravelDaysLCC + numTravelDays
            # print("")
            # print("")
        elif i["cityType"] == 'HCC':
            # print(f'Project: {i["cityType"]} City')
            # print("Name: ", i['name'])
            # print("Start Date: ", i['startDate'])
            # print("End Date: ", i['endDate'])
            # print("City Type: ", i['cityType'])
            hccStartDates.append(i['startDate'])
            hccEndDates.append(i['endDate'])
            if i["startDate"] == i["endDate"]:
                numDays = 1
                numTravelDays = 1
                numFullDays = 0
            else:
                numDays = end_date - start_date
                numDays = int(numDays.days + 1)
                numTravelDays = 2
                if numFullDays < 0:
                    numFullDays = 0
                print(numDays)
                # print(numFullDays)
            numFullDays = int(numDays - numTravelDays)
            numFullDaysHCC = numFullDaysHCC + numFullDays
            numTravelDaysHCC = numTravelDaysHCC + numTravelDays
            # print("")
            # print("")
        # else:
            # print("Error - City Type unavailable")
            # print("Name: ", i['name'])
            # print("Start Date: ", i['startDate'])
            # print("End Date: ", i['endDate'])
            # print("City Type: ", i['cityType'])
            # print("")
            # print("")

        num_days = num_days + numDays

    # Calculations
    reimbursement_lcc_td = numTravelDaysLCC * lcc_td_rr
    reimbursement_lcc_fd = numFullDaysLCC * lcc_fd_rr
    reimbursement_hcc_td = numTravelDaysHCC * hcc_td_rr
    reimbursement_hcc_fd = numFullDaysHCC * hcc_fd_rr
    
    # print reimbursement rates
    print("Start Dates: ", startDates)
    print("End Dates: ", endDates)
    print("Total Number of Days: ", num_days)
    print()
    print("LCC Start Dates: ", lccStartDates)
    print("LCC End Dates: ", lccEndDates)
    print("Number of Travel Days: ", numTravelDaysLCC)
    print("Reimbursement for LCC Travel Days : $", reimbursement_lcc_td)
    print("Number of Full Days: ", numFullDaysLCC)
    print("Reimbursement for LCC Full Days : $", reimbursement_lcc_fd)
    print()
    print("HCC Start Dates: ", hccStartDates)
    print("HCC End Dates: ", hccEndDates)
    print("Number of Travel Days: ", numTravelDaysHCC)
    print("Reimbursement for HCC Travel Days : $", reimbursement_hcc_td)
    print("Number of Full Days: ", numFullDaysHCC)
    print("Reimbursement for HCC Full Days : $", reimbursement_hcc_fd)
    print()
    print()
    print("Number of Employees : ", numEmployees)
    print("Employees include: ", listEmployees)

