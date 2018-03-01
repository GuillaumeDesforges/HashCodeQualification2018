"""Fonctions Score"""

from core import *
import numpy as np

def lenght(ride):
    return (dist(ride.start,ride.end))
    

def ratioScore(B,t,car,ride):
    timeToStart = dist(car.pos,ride.start)
    hereInTime = ((ride.tf - t) > (timeToStart+dist(ride.start,ride.end)))
    score = -1
    if hereInTime:
        hereForBonus = ((ride.ti - t)>timeToStart)
        totBenef = lenght(ride)
        if hereForBonus:
            totBenef += B
        time = (max(ride.ti,t+timeToStart) + lenght(ride)) - t
        score = totBenef / time
    return score
    
def eval_density(R,C,cars):
    mappe = np.ones((R//10,C//10))
    for car in cars:
        mappe[car.pos.x//10,car.pos.y//10] += 1
    return(mappe)



def evolutedScore(B,t,car,ride):
    timeToStart = dist(car.pos,ride.start)
    hereInTime = ((ride.tf - t) > (timeToStart+dist(ride.start,ride.end)))
    score = -1
    if hereInTime:
        hereForBonu,s = ((ride.ti - t)>timeToStart)
        totBenef = lenght(ride)
        if hereForBonus:
            totBenef += B
        time = (max(ride.ti,t+timeToStart) + lenght(ride)) - t
        score = totBenef / time
    return score
    
# if __name__==__main__:
#ride = Ride(1,1,5,5,1,20)
#car = Car()
#print(ratioScore(2,0,car,ride))
#print(dist(ride.start,ride.end))
