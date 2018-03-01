"""Fonctions Score"""

from core import *

def lenght(ride):
    return (abs(ride.x0-ride.x1) + abs(ride.y0-ride.y1))

def ratioScore(B,t,car,ride):
    baseBenef = lenght(ride)
    

