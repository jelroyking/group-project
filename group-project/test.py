import csv      #Imports the csv module
out=open("DataExtraction.csv","rt")   #Opens the csv file for reading
data=csv.reader(out)
data=[row for row in data]

date=[row[0] for row in data]          #Stores the data in their relevant lists
data_steps=[row[1] for row in data]
data_calories=[row[2] for row in data]
data_kilo=[row[6] for row in data]
del date[0]          #Deletes the 1st element of each list
del data_steps[0]
del data_calories[0]
del data_kilo[0]
steps=[int(x) for x in data_steps]        #Makes sure the data is of the correct data type
calories=[int(x) for x in data_calories]
kilo=[float(x) for x in data_kilo]
out.close()

def totalSteps():
  """A function to calculate the total number of steps taken by the watch user"""
  totalSteps=sum(steps)
  print()
  print("You have taken a total of ",totalSteps,"steps")
    
def totalCalories():
  """A function to calculate the total number of calories burned by the watch user"""
  totalCalories=sum(calories)
  print()
  print("You have burned a total of ",totalCalories,"calories")
    
def totalDistance():
  """A function to calculate the total distance travelled by the watch user"""
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

def stepsPerDay():
  """A function to display the number of steps taken each day"""
  listLength=len(steps)
  for x in range(listLength):
    print(steps[x])
    
def caloriesPerDay():
  """A function to display the number of calories burned each day"""
  listLength=len(calories)
  for x in range(listLength):
    print(calories[x])
    
def distancePerDay():
  """A function to display the distance travelled each day"""
  listLength=len(kilo)
  for x in range(listLength):
    print(kilo[x])
    
def maxSteps():
  """A function to calculate the largest number of steps taken in 1 day"""
  maxi=0
  listLength=len(steps)
  for x in range(listLength):
    if steps[x]>maxi:
      maxi=steps[x]
      pointer=x
  print()
  print("The largest number of steps taken in 1 day is",maxi,"steps, that was on the",date[pointer])
  
def maxCalories():
  """A function to calculate the largest number of calories burned in 1 day"""
  maxi=0
  listLength=len(calories)
  for x in range(listLength):
    if calories[x]>maxi:
      maxi=calories[x]
      pointer=x
  print()
  print("The largest number of calories burned in 1 day is",maxi,"calories, that was on the",date[pointer])
  
def maxDistance():
  """A function to calculate the greatest distance travelled in 1 day"""
  maxi=0
  listLength=len(kilo)
  for x in range(listLength):
    if kilo[x]>maxi:
      maxi=round(kilo[x],2)
      pointer=x
  print()
  print("The greatest distance travelled in 1 day is",maxi,"kilometers, that was on the",date[pointer])
  
def minSteps():
  """A function to calculate the smallest number of steps taken in 1 day"""
  mini=0
  listLength=len(steps)
  for x in range(listLength):
    if steps[x]<mini:
      mini=steps[x]
      #pointer=x
  print()
  print("The smallest number of steps taken in 1 day is",mini,"steps, that was on the",date[x])
  
def minCalories():
  """A function to calculate the smallest number of calories burned in 1 day"""
  mini=0
  listLength=len(calories)
  for x in range(listLength):
    if calories[x]<mini:
      mini=calories[x]
      #pointer=x
  print()
  print("The smallest number of calories burned in 1 day is",mini,"calories, that was on the",date[x])
  
def minDistance():
  """A function to calculate the smallest distance travelled in 1 day"""
  mini=0
  listLength=len(kilo)
  for x in range(listLength):
    if kilo[x]<mini:
      mini=round(kilo[x],2)
      #pointer=x
  print()
  print("The smallest distance travelled in 1 day is",mini,"kilometers, that was on the",date[x])
  

print("A: Steps")      #Displays the main menu
print("B: Calories")
print("C: Distance")
menuChoice=str(input("Select on of the above - "))  
if menuChoice == "A":
  print()
  print("A: Total number of steps")     #Displays the steps submenu
  print("B: Average number of steps")
  print("C: Steps per day")
  print("D: Most steps taken in a single day")
  print("E: Least steps taken in a single day")
  stepsMenuChoice=str(input("Select on of the above - "))
  if stepsMenuChoice == "A":
    totalSteps()
  elif stepsMenuChoice == "B":
    averageSteps()
  elif stepsMenuChoice == "C":
    stepsPerDay()
  elif stepsMenuChoice == "D":
    maxSteps()
  elif stepsMenuChoice == "E":
    minSteps()
elif menuChoice == "B":
  print()
  print("A: Total number of calories")    #Displays the calories submenu
  print("B: Average number of calories")
  print("C: Display calories per day")
  print("D: Most calories burned in a single day")
  print("E: Least calories burned in a single day")
  caloriesMenuChoice=str(input("Select on of the above - "))
  if caloriesMenuChoice == "A":
    totalCalories()
  elif caloriesMenuChoice == "B":
    averageCalories()
  elif caloriesMenuChoice == "C":
    caloriesPerDay()
  elif caloriesMenuChoice == "D":
    maxCalories()
  elif caloriesMenuChoice == "E":
    minCalories()
elif menuChoice == "C":
  print()
  print("A: Total distance")     #Displays the distance submenu
  print("B: Average distance")
  print("C: Distance per day")
  print("D: Greatest distance travelled in a single day")
  print("E: Least distance travelled in a single day")
  distanceMenuChoice=str(input("Select on of the above - "))
  if distanceMenuChoice == "A":
    totalDistance()
  elif distanceMenuChoice == "B":
    averageDistance()
  elif distanceMenuChoice == "C":
    distancePerDay()
  elif distanceMenuChoice == "D":
    maxDistance()
  elif distanceMenuChoice == "E":
    minDistance()
else:
  print()
  print("Please enter a valid menu option")



  