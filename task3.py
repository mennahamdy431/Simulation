import random
import numpy as np

count = 1000000

Time = list()
idealTimeList = list()


def random_0to1():
    return random.uniform(0, 1)


r1 = 0.0
r2 = 0.0
r3 = 0.0
Max = 0
Min = 0

for i in range(count):
    Time.append(10)
    MinTime = 10
    r1 = random_0to1()
    r2 = random_0to1()
    r3 = random_0to1()
    if 0 <= r1 < 0.4:
        Time[i] += 2
    if 0 <= r2 < 0.1:
        Time[i] += 1
    if 0 <= r2 < 0.7:
        Time[i] += 3

    Max = max(Time[i], Max)
    Min = min(Time[i], MinTime)

print("The worst case Time = ", Max, "\n")
print("The best case Time = ", Min, "\n")
print("The base case Time = ", sum(Time) / len(Time), "\n")


import random
import numpy as np
from datetime import timedelta

count = 1000000  # i change that count to 10 to get results and be able to compare between when count is 10 and 1000000

Time = list()
idealTimeList = list()


def random_0to1():
    return random.uniform(0, 1)


r1 = 0.0
r2 = 0.0
r3 = 0.0
Max = 0
Min = 0
Flag_1 = 0
Flag_2 = 0

for i in range(count):
    Time.append(10)
    MinTime = 10
    r1 = random_0to1()
    r2 = random_0to1()
    r3 = random_0to1()
    if 0 <= r1 < 0.4:
        Time[i] += 2
        Flag_1 = 1
    if Flag_1 == 1 and 0 <= r2 < 0.05:
        Time[i] += 1
        Flag_2 = 1
    elif Flag_1 == 0 and 0 <= r2 < 0.1:
        Time[i] += 1
        Flag_2 = 1
    if Flag_2 == 1 and 0 <= r3 < 0.4:
        Time[i] += 3
    elif Flag_2 == 0 and 0 <= r3 < 0.7:
        Time[i] += 3
    Max = max(Time[i], Max)
    Min = min(Time[i], MinTime)

leaving_time=timedelta(hours=8,minutes=0)-timedelta(hours=0,minutes=Max)
print("The leaving time : ",leaving_time)
print("Maximum Time = ", Max, "\n")
print("Minimum Time = ", Min, "\n")
print("Average Time = ", sum(Time) / len(Time), "\n")

