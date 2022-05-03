import random
import matplotlib.pyplot as plt
import tkinter.messagebox
from tkinter import *

customers = 500  # number of customers in all system

top = Tk()  # creating the main window
top.title('Simulation for queuing system')  # setting title of the window
top.geometry('300x100')  # setting the size of the window


def func():  # function of the button
    tkinter.messagebox.showinfo("Greetings", "HELLO! YOU SHOULD CLOSE THE TEXT BOX TO SEE THE RESULT OF SIMULATING.")


btn = Button(top, text="Simulate", width=17, height=3, command=func, fg='black', bg='blue')
btn.place(x=90, y=17)
top.mainloop()  # running the loop that works as a trigger


# Generate random number
def random_num():
    return random.uniform(0, 1)


# Generate random arrival time
def arrive_time():
    r = random_num()
    if r >= 0 and r < 0.09:
        at = 0
    elif r >= 0.09 and r < 0.28:
        at = 1
    elif r >= 0.28 and r < 0.58:
        at = 2
    elif r >= 0.58 and r < 0.79:
        at = 3
    elif r >= 0.79 and r < 0.91:
        at = 4
    else:
        at = 5
    return at


# Generate random Service time
def service_time():
    r = random_num()
    if r >= 0 and r < 0.2:
        st = 1
    elif r >= 0.2 and r < 0.6:
        st = 1
    elif r >= 0.6 and r < 0.8:
        st = 2
    elif r >= 0.8 and r < 0.9:
        st = 3
    else:
        st = 4
    return st


# Class Client that have all its operations Time
class Client:
    inter_arrival_time = 0
    arrival_time = 0
    service_time = 0
    service_start_time = 0
    WaitingTime = 0
    completion_time = 0
    total_time = 0
    inside_bank_teller = 0
    drive_in_teller = 0
    drive_in_TellerQ = 0

    def __init__(self):
        self.inter_arrival_time = 0
        self.ArrivalTime = 0
        self.service_time = 0
        self.service_start_time = 0
        self.WaitingTime = 0
        self.completion_time = 0
        self.total_time = 0
        self.inside_bank_teller = 0
        self.drive_in_teller = 0
        self.drive_in_TellerQ = 0

    def print(self):
        print("Inter arrival Time = ", self.inter_arrival_time)
        print("Arrival Time = ", self.ArrivalTime)
        print("Service Time = ", self.service_time)
        print("Service Start Time = ", self.service_start_time)
        print("Waiting Time = ", self.WaitingTime)
        print("Completion Time = ", self.completion_time)
        print("Total Time = ", self.total_time)
        print("Inside Bank Teller= ", self.inside_bank_teller)
        print("Drive-inTeller = ", self.drive_in_teller)
        print("Drive-in Teller Queue = ", self.drive_in_TellerQ)
        print("======================")
        return


# Function That take All Clients inside Bank and Calculate The max inside Queue Bank
def calc_max_in_queue(lst):
    ans = 0
    mx = 0
    for i in range(len(lst)):
        if lst[i].WaitingTime > 0:
            mx += 1
        else:
            mx = 0

        ans = max(ans, mx)
    return ans


avg_service_outside = []
avg_service_inside = []
avg_waiting_outside = []
avg_waiting_inside = []

# simulate the program 20 once
for j in range(20):

    sum_wait_outside = 0  # Store Sum wait Time outside Bank
    sum_wait_inside = 0  # Store Sum wait Time inside Bank
    sum_serve_inside = 0  # Store Sum Service Time outside Bank
    sum_serve_outside = 0  # Store Sum Service Time Inside Bank
    NumServeInside = 0  # Store Number of Clients Served inside Bank
    NumServeOutside = 0  # Store Number of Clients Served Outside Bank
    NumWaitInside = 0  # Store Number of Clients Waited inside Bank
    NumWaitOutside = 0  # Store Number of Clients Waited Outside Bank
    Idle = 0  # Calculate The portion of Idle Time
    all_clients = []  # Store All Client Come in The System
    all_inside_bank = []  # Store All Client Come Served inside Bank
    Time = 0  # Current unit time of the day

    for i in range(customers):  # simulate for 500 customer

        CurrClient = Client()
        InterTime = arrive_time()
        ServeTime = service_time()
        arrival_time = InterTime + Time
        CurrClient.inter_arrival_time = InterTime
        CurrClient.ArrivalTime = arrival_time
        CurrClient.service_time = ServeTime
        Time = arrival_time

        if i == 0:  # first client in driven-in teller

            CurrClient.service_start_time = CurrClient.ArrivalTime
            CurrClient.completion_time = CurrClient.service_start_time + CurrClient.service_time
            CurrClient.total_time = CurrClient.completion_time - CurrClient.ArrivalTime
            CurrClient.drive_in_teller = CurrClient.completion_time
            sum_serve_outside += CurrClient.service_time
            NumServeOutside += 1
        else:  # second client in driven-in teller

            PrevClient = all_clients[-1]

            # If the client arrived when the Drive-in teller is available
            if CurrClient.ArrivalTime >= PrevClient.drive_in_teller:

                CurrClient.service_start_time = CurrClient.ArrivalTime
                CurrClient.completion_time = CurrClient.service_start_time + CurrClient.service_time
                CurrClient.total_time = CurrClient.completion_time - CurrClient.ArrivalTime
                CurrClient.drive_in_teller = CurrClient.completion_time
                CurrClient.inside_bank_teller = PrevClient.inside_bank_teller
                CurrClient.drive_in_TellerQ = PrevClient.drive_in_TellerQ
                sum_serve_outside += CurrClient.service_time  # sum of time client spent in service in driver-in teller
                NumServeOutside += 1  # counter that count number of services in driver-in teller


            elif PrevClient.drive_in_teller > CurrClient.ArrivalTime >= PrevClient.drive_in_TellerQ:

                CurrClient.WaitingTime = PrevClient.drive_in_teller - CurrClient.ArrivalTime
                CurrClient.service_start_time = CurrClient.ArrivalTime + CurrClient.WaitingTime
                CurrClient.completion_time = CurrClient.service_start_time + CurrClient.service_time
                CurrClient.total_time = CurrClient.completion_time - CurrClient.ArrivalTime
                CurrClient.drive_in_teller = CurrClient.completion_time
                CurrClient.drive_in_TellerQ = CurrClient.service_start_time
                CurrClient.inside_bank_teller = PrevClient.inside_bank_teller
                sum_wait_outside += CurrClient.WaitingTime
                NumWaitOutside += 1
                sum_serve_outside += CurrClient.service_time
                NumServeOutside += 1

            else:

                CurrClient.WaitingTime = max(0, PrevClient.inside_bank_teller - CurrClient.ArrivalTime)
                CurrClient.service_start_time = CurrClient.ArrivalTime + CurrClient.WaitingTime
                CurrClient.completion_time = CurrClient.service_start_time + CurrClient.service_time
                CurrClient.total_time = CurrClient.completion_time - CurrClient.ArrivalTime
                CurrClient.drive_in_teller = PrevClient.drive_in_teller
                CurrClient.drive_in_TellerQ = PrevClient.drive_in_TellerQ
                CurrClient.inside_bank_teller = CurrClient.completion_time

                if CurrClient.WaitingTime != 0:
                    sum_wait_inside += CurrClient.WaitingTime
                    NumWaitInside += 1

                sum_serve_inside += CurrClient.WaitingTime
                NumServeInside += 1

                if len(all_inside_bank) > 1:
                    Idle += max(0, CurrClient.ArrivalTime - all_inside_bank[-1].completion_time)

                all_inside_bank.append(CurrClient)  # append the data of all clients who entered inside bank in a list

        all_clients.append(CurrClient)  # append the data of all clients in a list

    '''
    getting the statistical mean (average)
    '''
    def mean(total_sum, num):
        return total_sum / num


    print("The average service time outside bank = ", mean(sum_serve_outside, NumServeOutside), "Minute", "\n")
    avg_service_outside.append(mean(sum_serve_outside, NumServeOutside))
    print("The average service time inside bank = ", mean(sum_serve_inside, NumServeInside), "Minute", "\n")
    avg_service_inside.append(mean(sum_serve_inside, NumServeInside))
    print("The average waiting time inside bank = ", mean(sum_wait_inside, NumWaitInside), "Minute", "\n")
    avg_waiting_inside.append(mean(sum_wait_inside, NumWaitInside))
    print("The average waiting time outside bank = ", mean(sum_wait_outside, NumWaitOutside), "Minute", "\n")
    avg_waiting_outside.append(mean(sum_wait_outside, NumWaitOutside))
    print("The maximum inside-bank teller Queue = ", calc_max_in_queue(all_inside_bank), "client", "\n")
    print("The probability that a customer wait in the inside bank = ", mean(NumWaitInside, customers), "Minute", "\n")
    print("The portion of idle time of the inside-bank teller = ", Idle, "Minute", "\n")
    print("If the drive-in teller queue can accommodate for two cars instead of", "\n",
          " one car, the average waiting time inside the bank will decrease almost", "\n",
          " nonexistent but the average waiting time in drive-in teller will increase.")
    print("================================================================")

# Data Visualization(Plots)
plt.hist(avg_service_outside)
plt.title('Service in Driven-in teller')
plt.show()

plt.hist(avg_service_inside)
plt.title('Service in Bank')
plt.show()

plt.hist(avg_waiting_inside)
plt.title('Waiting in Driven-in teller')
plt.show()

plt.hist(avg_waiting_outside)
plt.xlabel('Number of iterators')
plt.ylabel('Mean of waiting outside')
plt.title('Waiting in Bank')
plt.show()
