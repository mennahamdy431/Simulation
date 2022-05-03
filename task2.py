# menna hamdy mahmoud
# 20190558

import random
import matplotlib.pyplot as plt

unsatisfied_Cost = 100
remaining_Cost = 50
Profit_Selling = 450
Profit = list()
x = list()


def rand():
    return random.uniform(0, 1)


def get_x():
    r = rand()
    if r >= 0 and r < 0.2:
       x = 0
    elif r >= 0.2 and r < 0.6:
       x = 1
    elif r >= 0.6 and r < 0.8:
       x = 2
    elif r >= 0.8 and r < 0.9:
       x = 3
    else:
       x = 4
    return x


for i in range(500):
    x.append(get_x())

for Order in range(1, 3):
    Available = 0
    for Week in range(500):
        Available += Order
        if x[Week] < Available:
            sold = x[Week]
            Available -= x[Week]
            loss = Available * remaining_Cost
        elif x[Week] > Available:
            sold = Available
            Available = 0
            loss = (x[Week] - sold) * unsatisfied_Cost
        else:
            sold = x[Week]
            Available = 0
            loss = 0
        revenue = sold * Profit_Selling
        profit = revenue - loss
        if profit >= 0:
            Profit.append(profit)
    if Order == 1:
        AvgProf1 = sum(Profit) / 500
        Profit.clear()
    else :
        AvgProf2 = sum(Profit) / 500
print("The average profit of 500 weeks is :")
print("if the shop owner ordered 1 PC per week :", AvgProf1)
print("if the shop owner ordered 2 PC per week :", AvgProf2)

if AvgProf1 > AvgProf2:
    print("Ordering 1 PC per week is the best decision")
elif AvgProf1 < AvgProf2:
    print("Ordering 2 PC per week is the best decision")
