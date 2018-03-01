#!/usr/bin/python

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(pt1, pt2):
    return(abs(pt1.x-pt2.x)+abs(pt1.y-pt2.y))


class Ride:
    def __init__(self, x0, y0, x1, y1, ti, tf):
        self.ini = Coords(x0,y0)
        self.fin = Coords(x1,y1)
        self.ti = ti
        self.tf = tf

    def __str__(self):
        return ' '.join([str(self.x0), str(self.y0), str(self.x1), str(self.y1), str(self.ti), str(self.tf)])

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.target = None

    def distance(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

def read(file_path):
    with open(file_path) as f:
        lines = [line.replace("\n", "") for line in f.readlines()]
        R, C, F, N, B, T = tuple(map(int, lines[0].split(" ")))
        rides = []
        for line in lines[1:]:
            ride = Ride(*tuple(map(int, line.split(" "))))
            rides.append(ride)
        return R, C, F, N, B, T, rides

# Example
def fscore0(B, t, car, ride):
    return 1

if __name__ == "__main__":
    print(*read("a_example.in"))
