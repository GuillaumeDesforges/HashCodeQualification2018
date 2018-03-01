from random import *
from collections import deque
from math import *
#!/usr/bin/python
from math import abs

def distance(x, y, a, b):
    return abs(x-a)+abs(y-b)

MU = 10

def display(rides):
    for r in rides:
        print(r)

def neighbour(solution):
    n = len(solution)
    k = randint(0, n)
    solution

comp_ti = lambda ride: (ride.ti, -ride.d)

R, C, F, N, B, T, rides = read("./a_example.in")
rides = deque(sorted(rides, key=comp_ti))
display(ord_rides)

#t_rides = [[] for i in range(T)]    # Rides beginning at time id
#for ride in t_rides:
#    t_rides[ride.ti].append(ride)

class Ride:
    def __init__(self, idx, x0, y0, x1, y1, ti, tf):
        self.idx = idx
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1       self.ti = ti
        self.tf = tf
        self.d = distance(x0, y0, x1, y1)

def Car2:
    def __init__(self, idx):
        self.time = 0   # availble afterward
        self.idx = idx
        self.x = 0  # position where available
        self.y = 0
        self.path = []  # path driven (idx of rides)

# available_cars = [[Car2(idx) for idx in range(N)]]  # Cars availble at time id
# available_cars.extend([[] for i in range(T-1)])
available_cars = deque([Car2(idx) for idx in range(N)])

car = available_cars.popleft()
while car.time < T:
    while true:
        ride = rides.popleft()
        #if ride.ti < car.time:
        #    continue
        if ride.ti >

    for i in range(ceil(N/MU)):
        for rides in t_rides[car.time+i]:
            ride = max(rides, lambda ride: ride.d)

    available_cars.append(car)
    car = available_cars.popleft()






for ride in ord_rides:
    if ride.d
