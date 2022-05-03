import random
import numpy as np
import matplotlib.pyplot as plt

sellingPrice = 249
administrativeCost = 400000
advertisingCost = 600000
totalCost = 1000000
count = 10**6
mu, Sigma = 15000, 4500
C1 = list()
C2 = list()
X = list()
Profit = list()
loss = 0
Max = 0
Min = 0


def Random():
    return random.uniform(0, 1)


def getC1():
    r1 = Random()
    if r1>0 and r1<0.1:
        c1=43
    elif r1>=0.1 and r1<0.3:
        c1=44
    elif r1>=0.3 and r1<0.7:
        c1=45
    elif r1>=0.7 and r1<0.9:
        c1=46
    else :
        c1=47
    return c1


def getC2():
    c2 = random.uniform(80,100)
    return c2


def getX():
    # noinspection PyUnresolvedReferences
    x = np.random.normal(15000,4500)
    return x


for i in range(count):
    c1 = getC1()
    C1.append(c1)
    c2 = getC2()
    C2.append(c2)
    x = getX()
    X.append(x)
    profit = ((249 - c1 - c2)*x) - 1000000
    if profit < 0:
        loss += 1
    else:
        Profit.append(profit)
    Max = max(profit, Max)
    Min = min(profit, Min)
print("Maximum Profit = ", Max)
print("Maximum Loss = ", -1 * Min)
print("Average Profit = ", sum(Profit)/len(Profit))
print("Probability of Loss = ", loss/count)

plt.hist(C1)
plt.show()

plt.hist(C2)
plt.show()

plt.hist(X)
plt.show()

plt.hist(Profit)
plt.show()
