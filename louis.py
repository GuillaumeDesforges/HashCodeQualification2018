"""Fonctions Score"""

from core import *

def lenght(ride):
    return (dist(ride.start,ride.end))

def ratioScore(B,t,car,ride):
    timeToStart = dis(car.pos,ride.start)
    hereInTime = ((ride.tf - t) > (timeToStart+dis(ride.start,ride.end)))
    score = -1
    if hereInTime:
        hereForBonus = ((ride.ti - t)>tAtteinte)
        totBenef = lenght(ride) + hereForBonus*B
        time = [max(ti,t+tAtteinte) + lenght(ride)] - t
        score = totBenf ./ time
    return score 
    

