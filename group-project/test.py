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
del date[0]                                 #Deletes the 1st element of each list
del data_steps[0]
del data_calories[0]
del data_kilo[0]
del data_sleeptime[0]
del data_HrLowest[0]
del data_HrHighest[0]
del data_HrAverage[0]
steps=[int(x) for x in data_steps]        #Makes sure the data is of the correct data type
calories=[int(x) for x in data_calories]
kilo=[float(x) for x in data_kilo]
sleep=[int(x) for x in data_sleeptime]
hrLowest=[int(x) for x in data_HrLowest]
hrHighest=[int(x) for x in data_HrHighest]
hrAverage=[int(x) for x in data_HrAverage]
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
  totalDistance=sum(distance)
  print()
  print("You have travelled a total of ",totalDistance,"kilometres")
  
def totalSleep():
    """A function to calculate the total hours of sleep taken by the user of the watch"""
    totalSleep=sum(sleep)
    minutes=totalSleep//60
    hours=minutes//60
    minutes=minutes-(hours*60)
    print()
    print("You have slept the total of", hours,"h",  minutes, "m")

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

def averageSleep():
    """A function to calculate the average hours of sleep
    taken each day by using the data extracted from the csv file"""
    totalSleep=sum(sleep)
    listLength=len(sleep)
    averageSleep=totalSleep/listLength
    minutes=averageSleep//60
    hours=minutes//60
    minutes=minutes-(hours*60)
    print()
    print("You have slept and average of",int(hours),"h",int(minutes),"m")
    
def averageHeartrate():
  """A function to calculate the average number of heartbeat taken each day by using the data extracted from the csv file"""
  totalAverage=sum(hrAverage)
  listLength=len(hrAverage)
  averageHeartrate=totalAverage/listLength
  print()
  print("you have an average heartrate of", averageHeartrate,"BPM a day")

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
    
def sleepPerDay():
  """A function to display the number of hours slept each day"""
  listLength=len(sleep)
  for x in range(listLength):
    minutes = sleep[x]//60
    hours = minutes//60
    minutes = minutes-(60*hours)
    print(hours,"h",minutes,"m")

def heartratePerDay():
  """A function to display the number of heartrate each day"""
  listlength=len(hrAverage)
  for x in range(listlength):
    print(str(date[x])+"- Average="+str(hrAverage[x])+" Highest="+str(hrHighest[x])+" Lowest="+str(hrLowest[x]))

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

def maxSleep():
  """A function to calculate the highest number of hours that the user of the watch has slept"""
  maxi=0
  listLength=len(sleep)
  for x in range(listLength):
    if sleep[x]>maxi:
      maxi=sleep[x]
      minutes=maxi//60
      hours=minutes//60
      minutes=minutes-(hours*60)
      pointer=x
  print()
  print("The most amount of hours slept in 1 day is "+str(hours)+"h "+str(minutes)+"m, that was on the" ,date[pointer])
    
def maxHeartrate():
  """A function to calculate the highest number of heartbeat that the user of the watch has"""
  maxi=0
  listlength=len(hrHighest)
  for x in range(listlength):
    if hrHighest[x]>maxi:
      maxi=hrHighest[x]
      pointer=x
  print()
  print("The highest heartrate in 1 day is",maxi,"BPM, that was on the",date[pointer])
       
def minSteps():
  """A function to calculate the smallest number of steps taken in 1 day"""
  mini=0
  listLength=len(steps)
  for x in range(listLength):
    if steps[x]<mini:
      mini=steps[x]
      pointer=x
  print()
  print("The smallest number of steps taken in 1 day is",mini,"steps, that was on the",date[pointer])
  
def minCalories():
  """A function to calculate the smallest number of calories burned in 1 day"""
  mini=0
  listLength=len(calories)
  for x in range(listLength):
    if calories[x]<mini:
      mini=calories[x]
      pointer=x
  print()
  print("The smallest number of calories burned in 1 day is",mini,"calories, that was on the",date[pointer])
  
def minDistance():
  """A function to calculate the smallest distance travelled in 1 day"""
  mini=10000
  listLength=len(kilo)
  for x in range(listLength):
    if kilo[x]<mini:
      mini=round(kilo[x],2)
      pointer=x
  print()
  print("The smallest distance travelled in 1 day is",mini,"kilometers, that was on the",date[pointer])
  
def minSleep():
  """A function to calculate the smallest number of hours that the user of the watch has slept"""
  mini=10000
  listLength=len(sleep)
  print(sleep)
  for x in range(listLength):
    if sleep[x]<mini:
      mini=sleep[x]
      print(mini)
      minutes=mini//60
      print(minutes)
      hours=minutes//60
      print(hours)
      minutes=minutes-(hours*60)
      print(minutes)
      pointer=x
  print("Done")
  #print()
  #print("The least amount of hours slept in 1 day is "+str(hours)+"h "+str(minutes)+"m, that was on the" ,date[pointer])
  
def minHeartrate():
  """A function to calculate the lowest number of heartbeat that the user of the watch has"""
  mini=10000
  listlength=len(hrLowest)
  for x in range(listlength):
    if hrLowest[x]<mini:
      mini=hrLowest[x]
      pointer=x
  print()
  print("The lowest heartrate in 1 day is",mini,"BPM, that was on the",date[pointer])
  
print("A: Steps")      #Displays the main menu
print("B: Calories")
print("C: Distance")
print("D: Sleep")
print("E: Heart Rate")
menuChoice=str(input("Select one of the above - "))  
if menuChoice == "A":
  print()
  print("A: Total number of steps")     #Displays the steps submenu
  print("B: Average number of steps")
  print("C: Steps per day")
  print("D: Most steps taken in a single day")
  print("E: Least steps taken in a single day")
  stepsMenuChoice=str(input("Select one of the above - "))
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
  caloriesMenuChoice=str(input("Select one of the above - "))
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
  distanceMenuChoice=str(input("Select one of the above - "))
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
elif menuChoice == "D":
  print()
  print("A: Total number of hours slept")     #Displays the steps submenu
  print("B: Average number of of hours slept")
  print("C: Hours slept per day")
  print("D: Most number of hours slept in a single day")
  print("E: Least number of hours slept in a single day")
  sleepMenuChoice=str(input("Select one of the above - "))
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
elif menuChoice == "E":
  print()  
  print("A: Average number of BPM")       #Displays the steps submenu
  print("B: BPM per day")
  print("C: Highest BPM taken in a single day")
  print("D: Lowest BMP taken in a single day")
  heartrateMenuChoice=str(input("Select one of the above - "))
  if heartrateMenuChoice == "A":
    averageHeartrate()
  elif heartrateMenuChoice == "B":
    heartratePerDay()
  elif heartrateMenuChoice == "C":
    maxHeartrate()
  elif heartrateMenuChoice == "D": 
    minHeartrate()


