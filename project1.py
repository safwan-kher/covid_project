# Step 1: import required modules
import csv
import copy
import random

# Step2 create a dictionary template

template = {
    "date":"",
    "new_cases":0,
    "deaths":0,
    "recovered":0
}

data = [] # Creating a list of days: to be filled from the file 

# Step3 : Open the CSV file and read the data
with open('project1/covid_data.csv', 'r') as file:
    reader = csv.reader(file) 
    next(reader) #  Skip the header row
    for row in reader:
        day_data = copy.deepcopy(template)
        day_data["date"] = row[0]
        day_data["new_cases"] = int(row[1])
        day_data["deaths"] = int(row[2])
        day_data["recovered"] = int(row[3])
        data.append(day_data)

# print(data)

# total_cases = sum(day["new_cases"] for day in data)
total_cases=0

for day in data:
    total_cases += day["new_cases"]

print(total_cases)

total_deaths = sum(day["deaths"] for day in data)

print(total_deaths)

total_recovered = sum(day["recovered"] for day in data)

print(total_recovered)

avarage = total_cases / len(data)
# how to guess the length of a list without 'len' function
counter = 0
for i in data:
    counter += 1 # counter = counter + 1
print(counter)

random_day = random.choice(data)
print(random_day['date'])
print(random_day['new_cases'])
print(random_day['deaths'])
print(random_day['recovered'])







