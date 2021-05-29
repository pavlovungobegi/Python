#A prisoner is trapped in a cell containing five doors. 
#The first door leads to a tunnel which returns to his cell after three days of travel. 
#The second leads to a tunnel which returns him to his cell after a single day of travel.
#The third door leads him immediately to freedom. 
#The fourth door leads to a tunnel that will take him to freedom after two days of travel and the fifth door leads to a tunnel that will take him to the beginning of the tunnel of the second door after three days of travel.
#Assuming that the prisoner will always select doors 1, 2, 3, 4 and 5 with probabilities 0.25, 0.15, 0.1, 0.2 and 0.3 respectively, 
#simulate the system for n=20, 50, 100, 500, 1000 times to compute the expected number and variance of days until the prisoner reaches freedom?
from random import choice

doors = [];
pickedDoors = [];

for a in range(5):
    doors.append(1);
for a in range(3):
    doors.append(2);
for a in range(2):
    doors.append(3);
for a in range(4):
    doors.append(4);
for a in range(6):
    doors.append(5);
    
daysToFreedom = 0;
totalDaysToFreedom = 0;

#N = 500;
N = [20,50,100,500,1000];

for n in N:
    totalDaysToFreedom = 0;
    for k in range(n):
        pickedDoors.clear();
        daysToFreedom = 0;
        for i in range (100):
            pickedDoor = choice(doors);
            pickedDoors.append(pickedDoor);
            if (pickedDoor == 1):
                daysToFreedom += 3;
            elif (pickedDoor ==2):
                daysToFreedom += 1;
            elif (pickedDoor == 3):
                #print("Freedom in " + str(daysToFreedom) + " days");
                totalDaysToFreedom += daysToFreedom;
                break;
            elif (pickedDoor == 4):
                daysToFreedom += 2;
                #print("Freedom in " + str(daysToFreedom) + " days");
                totalDaysToFreedom += daysToFreedom;
                break;
            elif (pickedDoor == 5):
                daysToFreedom += 4;
        #print(pickedDoors);
    
    print("Mean days to freedom for " + str(n) + " trials: " + str(totalDaysToFreedom / n));


