#Random comment
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

def totalSteps():
    totalSteps=sum(steps)
    print()
    print("You have taken a total of ",totalSteps,"steps")
    
def totalCalories():
    totalCalories=sum(calories)
    print()
    print("You have burned a total of ",totalCalories,"calories")
    
def totalDistance():
    totalDistance=sum(distance)
    print()
    print("You have travelled a total of ",totalDistance,"kilometres")
    
def averageSteps():
    """A function to calculate the average number of steps
    taken each day using the data extracted from the csv file"""
    totalSteps=sum(steps)
    listLength=len(steps)
    averageSteps=totalSteps/listLength
    print()
    print("You take an average of",averageSteps,"steps a day")
    return(averageSteps)

def averageCalories():
    """A function to calculate the average number of calories
    burned each day using the data extracted from the csv file"""
    totalCalories=sum(calories)
    listLength=len(calories)
    averageCalories=totalCalories/listLength
    print()
    print("You burn an average of",averageCalories,"calories a day")
    return(averageCalories)

def averageDistance():
    """A function to calculate the average
    distance travelled per day in kilometers"""
    totalKilo=sum(kilo)
    listLength=len(kilo)
    averageKilo=round(totalKilo/listLength,2)
    print()
    print("You travel an average of",averageKilo,"kilometers a day")
    return(averageCalories)

print("A: Steps")
print("B: Calories")
print("C: Distance")
menuChoice=str(input("Select on of the above - "))
if menuChoice == "A":
  print()
  print("A: Total number of steps")
  print("B: Average number of steps")
  stepsMenuChoice=str(input("Select on of the above - "))
  if stepsMenuChoice == "A":
    totalSteps()
  elif stepsMenuChoice == "B":
    averageSteps()
elif menuChoice == "B":
  print()
  print("A: Total number of calories")
  print("B: Average number of calories")
  caloriesMenuChoice=str(input("Select on of the above - "))
  if caloriesMenuChoice == "A":
    totalCalories()
  elif caloriesMenuChoice == "B":
    averageCalories()
elif menuChoice == "C":
  print()
  print("A: Total distance")
  print("B: Average distance")
  distanceMenuChoice=str(input("Select on of the above - "))
  if distanceMenuChoice == "A":
    totalDistance()
  elif distanceMenuChoice == "B":
    averageDistance()
else:
  print("Please enter a valid menu option")












