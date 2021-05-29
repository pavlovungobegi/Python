#A large car dealership employs a sales person where he works on commission.
#The dealership has three types of cars: luxury, midsize and compact.
#Data from past years show that the car sales per week and type of cars sold have the distributions given below.
#If the car sold is compact, the sales person is given a commission of $250.
#For a midsize car, the commission is either $400 or $500, depending on the model sold. 
#On the midsize cars, a commission of $400 is paid out of 40% of the time and $500 is paid out the other 60% of the time. 
#For a luxury car, commission is paid out according to three separate rates: $1000 with a probability of 35%, $1500 with a probability of 40%, and $2000 with a probability of 25%. 
#For a van, commission is paid according to the following rates: $2000 with a probability of 40% and $3000 with a probability of 60%.

# of cars sold , Probability Type of car sold,  Probability
#0 0.10 Compact 0.45
#1 0.10 Midsize 0.30
#2 0.15 Luxury 0.10
#3 0.20 Van 0.15
#4 0.20
#5 0.15
#6 0.10

# Simulate the system for 300 weeks to estimate the expected commission that a salesperson is paid in a week and compute the probability that the sales person earns a commission more than $10000 per week.

from random import choice

compactCommission = 250;
midsizeCommission = [400,400,500,500,500];
luxuryCommission = [];
for a in range(7):
    luxuryCommission.append(1000);
for a in range(8):
    luxuryCommission.append(1500);
for a in range(5):
    luxuryCommission.append(2000);
vanCommission = [2000,2000,3000,3000,3000];

carsSold = [0,0,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,6,6];
carType = [];
for a in range(9):
    carType.append("compact");
for a in range(6):
    carType.append("midsize");
for a in range(2):
    carType.append("luxury");
for a in range(3):
    carType.append("van");
    
weeklyCars = [];
weeklyCommission = 0;
totalCommission = 0;
weeksWithMoreThan10kCommission = 0;
numberOfWeeks = 300;

for k in range(numberOfWeeks):
    weeklyCars.clear();
    weeklySold = choice(carsSold);
    for i in range(weeklySold):
        weeklyCars.append(choice(carType));
        
    weeklyCommission = 0;
    for j in range(len(weeklyCars)):
        if (weeklyCars[j] == "compact"):
            weeklyCommission += 250;
        elif (weeklyCars[j] == "midsize"):
            weeklyCommission += choice(midsizeCommission);
        elif (weeklyCars[j] == "luxury"):
            weeklyCommission += choice(luxuryCommission);
        elif (weeklyCars[j] == "van"):
            weeklyCommission += choice(vanCommission);
    totalCommission += weeklyCommission;
    if (weeklyCommission >= 10000):
        weeksWithMoreThan10kCommission += 1;
            
print("Number of Weeks: " + str(numberOfWeeks) + "\nAverage Weekly Commission:" + str(totalCommission/numberOfWeeks) + "\nWeeks With More Than 10k Commission: "+ str(weeksWithMoreThan10kCommission) + "\nPossibility of More than 10k commission: " + str(weeksWithMoreThan10kCommission/300))
