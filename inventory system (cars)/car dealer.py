import random as rd
import numpy as np

inventory = 3
showroom = 4
reviewPeriod = 3
shortage = 0
maximum = 15
maximumShowroom = 5
maximumInventory = 10
last_day = 0
arrival_day = 0
order_cars = 0
ending_showroom = []
ending_inventory = []
demands_array = []
lead_time_array = []
theoretical_average_demand = (0+1+2+3+4)/5
experimental_average_demand = 0
theoretical_average_lead_time = (1+2+3)/3
experimental_average_lead_time = 0

days = int(input('Please enter the number of days.. : '))


def daily_demand():   
    global inventory
    global showroom
    global shortage
    # test_inventory = 0
    test_showroom = 0
    
    demands = rd.choices([0, 1, 2, 3, 4], [0.04, 0.30, 0.36, 0.16, 0.14])[0]
    demands_array.append(demands)
    test_inventory = inventory - demands
    inventory -= demands
    if test_inventory < 0:
        inventory = 0
        test_showroom = showroom + test_inventory
        showroom += test_inventory
    if test_showroom < 0:
        showroom = 0
        shortage += 1


def order(the_day):
    global arrival_day
    global last_day
    global order_cars
    
    if the_day % reviewPeriod == 0:
        last_day = the_day
        order_cars = maximum - showroom
        order_cars -= inventory
        arrival_day = last_day + order_arrival()


def order_arrival(): 
    arrival = rd.choices([1, 2, 3], [0.5, 0.35, 0.15])[0] 
    lead_time_array.append(arrival)
    return arrival


def fill_cars(the_day): 
    global inventory
    global showroom
    global order_cars
    if the_day == arrival_day:
        fill_showroom = maximumShowroom - showroom
        fill_inventory = maximumInventory - inventory
       
        order_cars -= fill_showroom
        showroom += fill_showroom
        if order_cars < 0:
            showroom += order_cars
            order_cars = 0
            return
        order_cars -= fill_inventory
        inventory += fill_inventory
        if order_cars < 0:
            inventory += order_cars
            order_cars = 0
            return


def calculate_ending():  
    ending_showroom.append(showroom)
    ending_inventory.append(inventory)


def show_ending():
    print("The average ending units in showroom :", np.mean(ending_showroom))
    print("The average ending units in inventory :", np.mean(ending_inventory))


def demand_matching():
    global experimental_average_demand
    global theoretical_average_demand
    print("theoretical average demand :", theoretical_average_demand)
    experimental_average_demand = np.mean(demands_array)
    print("experimental average demand :", experimental_average_demand)
    print("                                                           ")
    print("after different times of testing they are matching approximately")


def lead_time_matching():
    global experimental_average_lead_time
    global theoretical_average_lead_time
    print("theoretical average lead time :", theoretical_average_lead_time)
    experimental_average_lead_time = np.mean(lead_time_array)
    print("experimental average lead time :", experimental_average_lead_time)
    print("                                                           ")
    print("after different times of testing they are not approximately matching ")

   
for x in range(0, days, 1):
    order(x)
    fill_cars(x)
    daily_demand()
    calculate_ending()

 
show_ending()
print("The number of shortage days :", shortage)
demand_matching()
lead_time_matching()
print("After run on large day number")
print("we found that the the best value for review period is 4")
