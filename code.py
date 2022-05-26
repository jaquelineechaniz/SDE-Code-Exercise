# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:33:05 2022

Platform Science Code Exercise

@author: Jaqueline Echaniz
"""

def vowels(string):
	cont = 0
	for letter in string:
		if letter.lower() in "aeiou":
			cont += 1
	return cont

def consonants(string):
	cont = 0
	for letter in string:
		if letter.lower() in "bcdfghjklmnñpqrstvwxyz":
			cont += 1
	return cont

destinationFile = ''
driversFile = ''
destinations = []
drivers=[]

"Reading files"
while(destinationFile==''):
    print("Enter shipment destinations file path: ", end="")
    destinationFile=input()
    

while(driversFile==''):
    print("Enter drivers names file path: ", end="")
    driversFile=input()

try:
    with open(destinationFile, "r") as file:
        for line in file:
            line = line.replace('\n', '')
            destinations.append(line)
        pass
except:
    print("Invalid shipment destinations file path")


try:       
    with open(driversFile, "r") as file:
        for line in file:
            line = line.replace('\n', '')
            drivers.append(line)
        pass
except:
    print("Invalid drivers names file path")

"Data processing, measure string length, number of vowels and consonants"
destinationsArray = []

for element in destinations:
    data = {
        "Destination":element,
        "Length": len(element),
        "Assigned": False
        }
    destinationsArray.append(data)
    
driversArray = []
for element in drivers:
    data = {
        "Name":element,
        "Vowels": vowels(element),
        "Consonants": consonants(element),
        "Length": len(element),
        "Assigned":False
    }
    driversArray.append(data)

"Check if destinations name length matches driver name length"
deliveries = []

for destination in destinationsArray:
    for driver in driversArray:
        if destination["Length"]==driver["Length"] and driver["Assigned"]==False:
            delivery = {
                "Destination": destination["Destination"],
                "Driver": driver["Name"]
            }
            destination["Assigned"]=True
            driver["Assigned"]=True
            deliveries.append(delivery)
            break

contSameLength = len(deliveries)
            
"Keep only unassigned destinations and drivers"
auxDest = []
for destination in destinationsArray:
    if destination["Assigned"]==False:
        auxDest.append(destination)
        
destinationsArray = auxDest

auxDriv = []
for driver in driversArray:
    if driver["Assigned"]==False:
        auxDriv.append(driver)
    
driversArray = auxDriv

    
"Check which destinations are even and odd"
totalSS = 0
for destination in destinationsArray:
    delivery = {
        "Destination": '',
        "Driver": ''
    }
    basicSS = 0
    if destination["Assigned"]==False:
        if destination["Length"]%2 == 0:
            i = 0
            for index ,driver in enumerate(driversArray):
                auxSS = 0
                if driver["Assigned"]==False:
                    auxSS = driver["Vowels"]*1.5
                if auxSS > basicSS:
                    basicSS = auxSS
                    i=index
            if len(driversArray) > 0:
                driversArray[i]["Assigned"]=True
                delivery["Driver"] = driversArray[i]["Name"]
                driversArray.pop(i)
                destination["Assigned"]=True
                delivery["Destination"]=destination["Destination"]
                deliveries.append(delivery)
                totalSS = totalSS + basicSS
    

for destination in destinationsArray:
    delivery = {
        "Destination": '',
        "Driver": ''
    }
    if destination["Assigned"]==False:
        i = 0
        for index, driver in enumerate(driversArray):
            auxSS=0
            if driver["Assigned"]==False:
                auxSS=driver["Consonants"]*1
            if auxSS > basicSS:
                basicSS = auxSS
                i=index  
        if len(driversArray) > 0:
            driversArray[i]["Assigned"]=True
            delivery["Driver"] = driversArray[i]["Name"]
            driversArray.pop(i)
            destination["Assigned"]=True
            delivery["Destination"]=destination["Destination"]
            deliveries.append(delivery)
            totalSS = totalSS + basicSS
        
  
"Calculate the 50% increase depending on the number of destinations/drivers that match the name length"
for i in range(contSameLength):
    totalSS = totalSS * 1.5
    
    
"Print results"
print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("Total suitability score: ", totalSS)
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
print("ASSIGNMENT OF SHIPMENT DESTINATIONS AND DRIVERS\n")

for delivery in deliveries:
    print("Destination: ", delivery["Destination"], "|\tDriver: ", delivery["Driver"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



















































