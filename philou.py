from random import *
from collections import deque
from math import *
#!/usr/bin/python

def distance(x, y, a, b):
    return abs(x-a)+abs(y-b)

class Ride:
    def __init__(self, idx, x0, y0, x1, y1, ti, tf):
        self.idx = idx
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.ti = ti
        self.tf = tf
        self.d = distance(x0, y0, x1, y1)

    def __str__(self):
        return ' '.join([str(self.x0), str(self.y0), str(self.x1), str(self.y1), str(self.ti), str(self.tf)])

def read(file_path):
    with open(file_path) as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
        R, C, F, N, B, T = tuple(map(int, lines[0].split(" ")))
        rides = []
        for idx, line in enumerate(lines[1:]):
            ride = Ride(idx, *tuple(map(int, line.split(" "))))
            rides.append(ride)
        return R, C, F, N, B, T, rides

class Car:
    def __init__(self, idx):
        self.time = 0   # availble afterward
        self.idx = idx
        self.x = 0  # position where available
        self.y = 0
        self.path = []  # path driven (idx of rides)

    def __str__(self):
        return " ".join([str(self.time), str(self.idx), str(self.x), str(self.y), str(self.path)])

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

#t_rides = [[] for i in range(T)]    # Rides beginning at time id
#for ride in t_rides:
#    t_rides[ride.ti].append(ride)

# available_cars = [[Car2(idx) for idx in range(N)]]  # Cars availble at time id
# available_cars.extend([[] for i in range(T-1)])
available_cars = deque([Car(idx) for idx in range(F)])

def score(car, ride):
    pass

car = available_cars.popleft()
again = True
while car.time < T:
    waiting_zone = []
    print("Car :", car)
    while rides:
        ride = rides.popleft()
        print(len(rides), len(available_cars))
        print("- Ride :", ride)
        di = distance(ride.x0, ride.y0, car.x, car.y)
        if di+ride.d+car.time < ride.tf:
            car.path.append(ride.idx)
            car.time = max(ride.ti, car.time+di)
            available_cars.append(car)
            rides.extendleft(waiting_zone[max(0, len(waiting_zone)-MU):])
            break
        waiting_zone.append(ride)
    else:
        break
    car = available_cars.popleft()
