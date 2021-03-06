import csv      #Imports the csv module
out=open("DataExtraction2.csv","rt")   #Opens the csv file for reading
data=csv.reader(out)
data=[row for row in data]

date=[row[0] for row in data]          #Stores the data in their relevant lists
data_steps=[row[1] for row in data]
data_calories=[row[2] for row in data]
data_kilo=[row[6] for row in data]
data_sleeptime=[row [14] for row in data]
data_HrLowest=[row[3] for row in data]
data_HrHighest=[row[4] for row in data]
data_HrAverage=[row[5] for row in data]
data_workoutTime=[row[28] for row in data]
data_workoutCalories=[row[29] for row in data]
del date[0]                                 #Deletes the 1st element of each list
del data_steps[0]
del data_calories[0]
del data_kilo[0]
del data_sleeptime[0]
del data_HrLowest[0]
del data_HrHighest[0]
del data_HrAverage[0]
del data_workoutTime[0]
del data_workoutCalories[0]
steps=[int(x) for x in data_steps]        #Makes sure the data is of the correct data type
calories=[int(x) for x in data_calories]
kilo=[float(x) for x in data_kilo]
sleep=[int(x) for x in data_sleeptime]
hrLowest=[int(x) for x in data_HrLowest]
hrHighest=[int(x) for x in data_HrHighest]
hrAverage=[int(x) for x in data_HrAverage]
workoutTime=[x for x in data_workoutTime]
workoutCalories=[x for x in data_workoutCalories]
out.close()                             #Closes the csv file

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
  totalDistance=round(sum(kilo),2)
  print()
  print("You have travelled a total of ",totalDistance,"kilometres")
  
def totalSleep():
    """A function to calculate the total hours of sleep taken by the user of the watch"""
    totalSleep=sum(sleep)
    minutes=totalSleep//60  #converts the time in seconds to hours and minutes 
    hours=minutes//60
    minutes=minutes-(hours*60)
    print()
    print("You have slept the total of "+str(hours)+"h "+str(minutes)+"m")

def averageSteps():
  """A function to calculate the average number of steps
  taken each day using the data extracted from the csv file"""
  totalSteps=sum(steps)
  listLength=len(steps)
  averageSteps=totalSteps//listLength
  print()
  print("You take an average of",averageSteps,"steps a day")
  return(averageSteps)

def averageCalories():
  """A function to calculate the average number of calories
  burned each day using the data extracted from the csv file"""
  totalCalories=sum(calories)
  listLength=len(calories)
  averageCalories=totalCalories//listLength
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

def averageSleep():
    """A function to calculate the average hours of sleep
    taken each day by using the data extracted from the csv file"""
    totalSleep=sum(sleep)
    listLength=len(sleep)
    averageSleep=totalSleep//listLength
    minutes=averageSleep//60  #converts the average time in seconds to hours and minutes 
    hours=minutes//60
    minutes=minutes-(hours*60)
    print()
    print("You sleep an average of "+str(hours)+"h "+str(minutes)+"m each day")
    
def averageHeartrate():
  """A function to calculate the average number of heartbeat taken each day by using the data extracted from the csv file"""
  totalAverage=sum(hrAverage)
  listLength=len(hrAverage)
  averageHeartrate=totalAverage/listLength
  print()
  print("you have an average heartrate of", averageHeartrate,"BPM a day")
  
def averageWorkout():
  """A function to display the average length and average number of calories burned in a single workout"""
  listLength=len(workoutTime) #initialises the local variables
  noOfWorkouts=0
  totalTime=0
  totalCal=0
  for x in range(listLength):
    if (workoutTime[x]!=""):  #if the list element isn't empty
      totalTime=totalTime+int(workoutTime[x])
      noOfWorkouts=noOfWorkouts+1  #increments the counter by 1 
  averageTime=totalTime//noOfWorkouts
  minutes=averageTime//60  #converts the time in seconds to hours and minutes
  hours=minutes//60
  minutes=minutes-(60*hours)
  for x in range(listLength):
    if (workoutCalories[x]!=""):  #if the list element isn't empty
      totalCal=totalCal+int(workoutCalories[x])
  averageCal=totalCal//noOfWorkouts
  print()
  print("Average workout time = "+str(hours)+"h "+str(minutes)+"m")
  print()
  print("Average calories burned per workout =",averageCal)
  print()

def stepsPerDay():
  """A function to display the number of steps taken each day"""
  listLength=len(steps)
  for x in range(listLength):
    print(date[x],"-",steps[x])
    
def caloriesPerDay():
  """A function to display the number of calories burned each day"""
  listLength=len(calories)
  for x in range(listLength):
    print(date[x],"-",calories[x])
    
def distancePerDay():
  """A function to display the distance travelled each day"""
  listLength=len(kilo)
  for x in range(listLength):
    print(date[x],"-",round(kilo[x],2),"km")
    
def sleepPerDay():
  """A function to display the number of hours slept each day"""
  listLength=len(sleep)
  for x in range(listLength):
    minutes = sleep[x]//60
    hours = minutes//60
    minutes = minutes-(60*hours)
    print(date[x],"-"+str(hours)+"h "+str(minutes)+"m")

def heartratePerDay():
  """A function to display the number of heartrate each day"""
  listlength=len(hrAverage)
  for x in range(listlength):
    print(str(date[x])+"- Average="+str(hrAverage[x])+" Highest="+str(hrHighest[x])+" Lowest="+str(hrLowest[x]))
    
def displayWorkouts():
  """A function to display the time and calories burned for each workout"""
  listLength=len(workoutTime)
  for x in range(listLength):
    if (workoutTime[x]!=""):  #if the list element isn't empty
      minutes = int(workoutTime[x])//60  #converts the time in seconds to hours and minutes 
      hours = minutes//60
      minutes = minutes-(60*hours)
      print(date[x],"-","Time = "+str(hours)+"h "+str(minutes)+"m, Calories =",workoutCalories[x])

def maxSteps():
  """A function to calculate the largest number of steps taken in 1 day"""
  maxi=0
  listLength=len(steps)
  for x in range(listLength):
    if steps[x]>maxi:
      maxi=steps[x]
      pointer=x #stores the subscript of the new max steps
  print()
  print("The largest number of steps taken in 1 day is",maxi,"steps, that was on the",date[pointer])
  
def maxCalories():
  """A function to calculate the largest number of calories burned in 1 day"""
  maxi=0
  listLength=len(calories)
  for x in range(listLength):
    if calories[x]>maxi:
      maxi=calories[x]
      pointer=x  #stores the subscript of the new max calories 
  print()
  print("The largest number of calories burned in 1 day is",maxi,"calories, that was on the",date[pointer])
  
def maxDistance():
  """A function to calculate the greatest distance travelled in 1 day"""
  maxi=0
  listLength=len(kilo)
  for x in range(listLength):
    if kilo[x]>maxi:
      maxi=round(kilo[x],2)  #rounds maxi to an appropriate degree of accuracy 
      pointer=x #stores the subscript of the new max kilo
  print()
  print("The greatest distance travelled in 1 day is",maxi,"kilometers, that was on the",date[pointer])

def maxSleep():
  """A function to calculate the greatest number of hours that the user of the watch has slept in 1 day"""
  maxi=0
  listLength=len(sleep)
  for x in range(listLength):
    if sleep[x]>maxi:
      maxi=sleep[x]
      minutes=maxi//60  #converts the time in seconds to hours and minutes
      hours=minutes//60
      minutes=minutes-(hours*60)
      pointer=x  #stores the subscript of the new max sleep
  print()
  print("The greatest number of hours slept in 1 day is "+str(hours)+"h "+str(minutes)+"m, that was on the" ,date[pointer])
    
def maxHeartrate():
  """A function to calculate the highest number of heartbeat that the user of the watch has"""
  maxi=0
  listlength=len(hrHighest)
  for x in range(listlength):
    if hrHighest[x]>maxi:
      maxi=hrHighest[x]
      pointer=x  #stores the subscript of the new max hrHighest
  print()
  print("The highest heartrate in 1 day is",maxi,"BPM, that was on the",date[pointer])
  
def maxWorkout():
  """A function to display the longest workout and the workout with the most calories burned"""
  maxTime=0
  maxCal=0
  listlength1=len(workoutTime)
  listLength2=len(workoutCalories)
  for x in range(listlength1):
    if (workoutTime[x]!=""):  #if the list element isn't empty
      if (int(workoutTime[x])>int(maxTime)):
        maxTime=int(workoutTime[x])
        minutes=maxTime//60  #converts the time in seconds to hours and minutes
        hours=minutes//60
        minutes=minutes-(60*hours)
        pointer1=x  #stores the subscript of the new max workoutTime
  for x in range(listLength2):
    if (workoutCalories[x]!=""):  #if the list element isn't empty
      if (int(workoutCalories[x])>int(maxCal)):
        maxCal=int(workoutCalories[x])
        pointer2=x #stores the subscript of the new max workoutCalories
  print()
  print("Longest workout length is "+str(hours)+"h "+str(minutes)+"m, that was on the",date[pointer1])
  print()
  print("largest number of calories burned in a workout is",maxCal,"calories, that was on the", date[pointer2])
       
def minSteps():
  """A function to calculate the smallest number of steps taken in 1 day"""
  mini=100000
  listLength=len(steps)
  for x in range(listLength):
    if steps[x]<mini:  #tests if the list element is smaller than the current mini
      mini=steps[x]  #assigns the value of the current list element to mini
      pointer=x  #stores the subscript of the new min steps
  print()
  print("The smallest number of steps taken in 1 day is",mini,"steps, that was on the",date[pointer])
  
def minCalories():
  """A function to calculate the smallest number of calories burned in 1 day"""
  mini=10000
  listLength=len(calories)
  for x in range(listLength):
    if calories[x]<mini:  #tests if the list element is smaller than the current mini 
      mini=calories[x]  #assigns the value of the current list element to mini
      pointer=x  #stores the subscript of the new min calories 
  print()
  print("The smallest number of calories burned in 1 day is",mini,"calories, that was on the",date[pointer])
  
def minDistance():
  """A function to calculate the smallest distance travelled in 1 day"""
  mini=10000
  listLength=len(kilo)
  for x in range(listLength):
    if kilo[x]<mini:  #tests if the current list element is smaller than the current mini
      mini=round(kilo[x],2)  #assigns the value of the current list element to mini with an appropriate degree of accuracy 
      pointer=x  #stores the subscript of the new min kilo
  print()
  print("The smallest distance travelled in 1 day is",mini,"kilometers, that was on the",date[pointer])
  
def minSleep():
  """A function to calculate the smallest number of hours that the user of the watch has slept"""
  mini=100000
  listLength=len(sleep)
  for x in range(listLength):
    if sleep[x]<mini:  #tests if the current list element is smaller than the current mini
      mini=sleep[x]  #assigns the value of the current list element to mini
      minutes=mini//60  #converts the time in seconds to hours and minutes 
      hours=minutes//60
      minutes=minutes-(hours*60)
      pointer=x  #stores the subscript of the new min sleep
  print()
  print("The shortest amount of time slept in 1 day is "+str(hours)+"h "+str(minutes)+"m, that was on the",date[pointer])
  
def minHeartrate():
  """A function to calculate the lowest number of heartbeat that the user of the watch has"""
  mini=10000
  listlength=len(hrLowest)
  for x in range(listlength):
    if hrLowest[x]<mini:
      mini=hrLowest[x]
      pointer=x  #stores the subscript of the new min hrLowest
  print()
  print("The lowest heartrate in 1 day is",mini,"BPM, that was on the",date[pointer])
  
def minWorkout():
  """A function to display the shortest workout and the workout with the least calories burned"""
  minTime=10000
  minCal=10000
  listlength1=len(workoutTime)
  listLength2=len(workoutCalories)
  for x in range(listlength1):
    if (workoutTime[x]!=""):  #if the list element isn't empty 
      if (int(workoutTime[x])<int(minTime)):  #tests if the value of the current list element is samller than minTime
        minTime=int(workoutTime[x])
        minutes=minTime//60  #converts the time in seconds to hours and minutes 
        hours=minutes//60
        minutes=minutes-(60*hours)
        pointer1=x  #stores the subscript of the new min workoutTime
  for x in range(listLength2):
    if (workoutCalories[x]!=""):  #if the list element isn't empty 
      if (int(workoutCalories[x])<int(minCal)):  #tests if the value of the current list element is samller than minCal
        minCal=int(workoutCalories[x])  
        pointer2=x  #stores the subscript of the new min workoutCalories
  print()
  print("Shortest workout length is "+str(hours)+"h "+str(minutes)+"m, that was on the",date[pointer1])
  print()
  print("Smallest number of calories burned in a workout is",minCal,"calories, that was on the", date[pointer2])
  
print("A: Steps")      #Displays the main menu
print("B: Calories")
print("C: Distance")
print("D: Sleep")
print("E: Heart Rate")
print("F: Workout")
menuChoice=str(input("Select one of the above - "))  #stores the user input
menuChoice=menuChoice.upper()  #Converts the user input to uppercase 
if menuChoice == "A":
  print()
  print("A: Total number of steps")     #Displays the steps submenu
  print("B: Average number of steps")
  print("C: Steps per day")
  print("D: Most steps taken in a single day")
  print("E: Least steps taken in a single day")
  stepsMenuChoice=str(input("Select one of the above - "))  #stores the user input
  stepsMenuChoice=stepsMenuChoice.upper()  #Converts the user input to uppercase
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
  else:  #incase the user enters an inappropriate value
    print()
    print("Error - Please enter one of the options from the menu")
elif menuChoice == "B":
  print()
  print("A: Total number of calories")    #Displays the calories submenu
  print("B: Average number of calories")
  print("C: Display calories per day")
  print("D: Most calories burned in a single day")
  print("E: Least calories burned in a single day")
  caloriesMenuChoice=str(input("Select one of the above - "))  #stores the user input
  caloriesMenuChoice=caloriesMenuChoice.upper()  #Converts the user input to uppercase
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
  else:  #incase the user enters an inappropriate value
    print()
    print("Error - Please enter one of the options from the menu")
elif menuChoice == "C":
  print()
  print("A: Total distance")     #Displays the distance submenu
  print("B: Average distance")
  print("C: Distance per day")
  print("D: Greatest distance travelled in a single day")
  print("E: Least distance travelled in a single day")
  distanceMenuChoice=str(input("Select one of the above - "))  #stores the user input
  distanceMenuChoice=distanceMenuChoice.upper()  #Converts the user input to uppercase
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
  else:  #incase the user enters an inappropriate value
    print()
    print("Error - Please enter one of the options from the menu")
elif menuChoice == "D":
  print()
  print("A: Total number of hours slept")     #Displays the steps submenu
  print("B: Average number of of hours slept")
  print("C: Hours slept per day")
  print("D: Greatest number of hours slept in a single day")
  print("E: Least number of hours slept in a single day")
  sleepMenuChoice=str(input("Select one of the above - "))  #stores the user input
  sleepMenuChoice=sleepMenuChoice.upper()  #Converts the user input to uppercase
  if sleepMenuChoice == "A":
    totalSleep()
  elif sleepMenuChoice == "B":
    averageSleep()
  elif sleepMenuChoice == "C":
    sleepPerDay()
  elif sleepMenuChoice == "D":
    maxSleep()
  elif sleepMenuChoice == "E":
    minSleep()
  else:  #incase the user enters an inappropriate value
    print()
    print("Error - Please enter one of the options from the menu")
elif menuChoice == "E":
  print()  
  print("A: Average number of BPM")       #Displays the steps submenu
  print("B: BPM per day")
  print("C: Highest BPM taken in a single day")
  print("D: Lowest BMP taken in a single day")
  heartrateMenuChoice=str(input("Select one of the above - "))  #stores the user input
  heartrateMenuChoice=heartrateMenuChoice.upper()  #Converts the user input to uppercase
  if heartrateMenuChoice == "A":
    averageHeartrate()
  elif heartrateMenuChoice == "B":
    heartratePerDay()
  elif heartrateMenuChoice == "C":
    maxHeartrate()
  elif heartrateMenuChoice == "D": 
    minHeartrate()
  else:  #incase the user enters an inappropriate value
    print()
    print("Error - Please enter one of the options from the menu")
elif menuChoice == "F":
  print()
  print("A: Display all workouts")
  print("B: Average workout time and calories burned")
  print("C: Highest workout time and calories burned")
  print("D: Lowest workout time and calories burned")
  workoutMenuChoice=str(input("Select one of the above - "))  #stores the user input
  workoutMenuChoice=workoutMenuChoice.upper()  #Converts the user input to uppercase
  if workoutMenuChoice == "A":
    displayWorkouts()
  elif workoutMenuChoice == "B":
    averageWorkout()
  elif workoutMenuChoice == "C":
    maxWorkout()
  elif workoutMenuChoice == "D": 
    minWorkout()
  else:  #incase the user enters an inappropriate value
    print()
    print("Error - Please enter one of the options from the menu")
else:  #incase the user enters an inappropriate value
  print()
  print("Error - Please enter one of the options from the menu")