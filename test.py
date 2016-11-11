import csv
out=open("DataExtraction.csv","rt")
data=csv.reader(out)
data=[row for row in data]

date=[row[0] for row in data]
data_steps=[row[1] for row in data]
data_calories=[row[2] for row in data]
data_kilo=[row[6] for row in data]
del date[0]
del data_steps[0]
del data_calories[0]
del data_kilo[0]
steps=[int(x) for x in data_steps]
calories=[int(x) for x in data_calories]
kilo=[float(x) for x in data_kilo]
out.close()

def averageSteps():
    """A function to calculate the average number of steps
    taken each day using the data extracted from the csv file"""
    totalSteps=sum(steps)
    listLength=len(steps)
    averageSteps=totalSteps/listLength
    print("You take an average of",averageSteps,"steps a day")
    return(averageSteps)

def averageCalories():
    """A function to calculate the average number of calories
    burned each day using the data extracted from the csv file"""
    totalCalories=sum(calories)
    listLength=len(calories)
    averageCalories=totalCalories/listLength
    print("You burn an average of",averageCalories,"calories a day")
    return(averageCalories)

def averageDistance():
    """A function to calculate the average
    distance travelled per day in kilometers"""
    totalKilo=sum(kilo)
    listLength=len(kilo)
    averageKilo=round(totalKilo/listLength,2)
    print("You travel an average of",averageKilo,"kilometers a day")
    return(averageCalories)

print("A: Average steps taken")
print("B: Average calories burned")
print("C: Average distance travelled")
option=input("Please select one of the above options - ")
if option=="A":
    averageSteps()
elif option=="B":
    averageCalories()
elif option=="C":
    averageDistance()
else:
    print("Please enter a valid option")