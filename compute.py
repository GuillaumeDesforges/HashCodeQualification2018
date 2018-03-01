#!/usr/bin/python
from core import *
from glouton import *

from louis import ratioScore

instances = [
        "a_example",
        "b_should_be_easy",
        "c_no_hurry",
        "d_metropolis",
        "e_high_bonus"
        ]

for instance in instances:
    print(instance)
    R, C, F, N, B, T, rides = read(instance+".in")
    solution = glouton(R, C, F, N, B, T, rides, ratioScore)
    write(instance+".out", solution)
