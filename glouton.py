#!/usr/bin/python
from core import *

def start(B, t, car, rides, fscore):
    if len(rides) == 0:
        return
    score_rides = [(ride, fscore(B, t, car, ride)) for ride in rides]
    best_ride = max(score_rides, key=lambda k:k[1])[0]
    car.requested = best_ride
    car.t_busy = dist(car.pos, best_ride.start)
    rides.remove(best_ride)
    print(rides)


def glouton(R, C, F, N, B, T, rides, fscore):
    cars = [Car() for i in range(F)]
    for car in cars:
        start(B, 0, car, rides, fscore)
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
                    print("{} FIN Voiture arrivée en {} {}".format(t, ride.end.x, ride.end.y))
                    car.pos = ride.end
                    start(B, t, car, rides, fscore)
                    # TODO POINTS
                if car.requested is not None:
                    # Arrive pour le pickup d'une course
                    ride = car.requested
                    car.requested = None
                    car.ride = ride
                    print("{} DEB Voiture arrivée en {} {}".format(t, ride.start.x, ride.start.y))
                    car.pos = ride.start
                    car.t_busy = max(0, ride.ti - t) + dist(car.pos, ride.end)
                # TODO chercher le meilleur bail TMTC
                # et l'assigner à car.requested
                if car.ride is None and car.requested is None:
                    start(B, t, car, rides, fscore)

if __name__ == "__main__":
    R, C, F, N, B, T, rides = read("a_example.in")
    print(R, C, F, N, B, T, rides)
    glouton(R, C, F, N, B, T, rides, fscore0)
