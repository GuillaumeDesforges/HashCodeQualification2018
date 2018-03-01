#!/usr/bin/python
from core import *

def glouton(R, C, F, N, B, T, rides, fscore):
    cars = [Car() for i in range(F)]
    for t in range(T):
        for car in cars:
            if car.t_busy > 0:
                # Voiture en trajet
                car.t_busy = car.t_busy - 1
            elif car.t_busy == 0:
                # Arrive a destination
                if car.ride is not None:
                    # Arrive a la fin d'une course
                    ride = car.ride
                    car.ride = None
                    print("FIN Voiture arrivée en {} {}".format(ride.x1, ride.y1))
                    car.pos = ride.end
                    # TODO POINTS
                if car.requested is not None:
                    # Arrive pour le pickup d'une course
                    ride = car.requested
                    car.ride = ride
                    car.requested = None
                    print("DEB Voiture arrivée en {} {}".format(ride.x0, ride.y0))
                    car.pos = ride.ini
                    car.t_busy = car.distance(ride.x0, ride.y0)
                # TODO chercher le meilleur bail TMTC
                # et l'assigner à car.requested
            else:


if __name__ == "__main__":
    R, C, F, N, B, T, rides = 
    glouton(*read("a_example.in"), fscore0)
