#!/usr/bin/python
from core import *
from louis import eval_density, evolutedScore

def start(B, t, car, rides, fscore, solution, density):
    if len(rides) == 0:
        return
    score_rides = [(ride, fscore(B, t, car, ride, density)) for ride in rides]
    best_ride = max(score_rides, key=lambda k:k[1])[0]
    car.requested = best_ride
    car.t_busy = dist(car.pos, best_ride.start)
    rides.remove(best_ride)
    solution[car.i].append(best_ride.i)
    # debug print(rides)


def glouton_density(R, C, F, N, B, T, rides, fscore):
    solution = [[] for i in range(F)]
    cars = [Car(i) for i in range(F)]
    density = eval_density(R, C, cars)
    for car in cars:
        start(B, 0, car, rides, fscore, solution, density)
    for t in range(T):
        density = eval_density(R, C, cars)
        for car in cars:
            if car.t_busy > 0:
                # Voiture en trajet
                car.t_busy = car.t_busy - 1
            if car.t_busy == 0:
                # Arrive a destination
                if car.ride is not None:
                    # Arrive a la fin d'une course
                    ride = car.ride
                    car.ride = None
                    # print("{} FIN {} Voiture {} arrivée en {} {}".format(t, ride.i, car.i, ride.end.x, ride.end.y))
                    car.pos = ride.end
                    start(B, t, car, rides, fscore, solution, density)
                if car.requested is not None:
                    # Arrive pour le pickup d'une course
                    ride = car.requested
                    car.requested = None
                    car.ride = ride
                    # print("{} DEB {} Voiture {} arrivée en {} {}".format(t, ride.i, car.i, ride.start.x, ride.start.y))
                    car.pos = ride.start
                    car.t_busy = max(0, ride.ti - t) + dist(car.pos, ride.end)
                if car.ride is None and car.requested is None:
                    # Si aucune course en cours, on passe à la suivante
                    start(B, t, car, rides, fscore, solution, density)
    return solution

if __name__ == "__main__":
    instance = "b_should_be_easy"
    R, C, F, N, B, T, rides = read(instance+".in")
    print(R, C, F, N, B, T, rides)
    solution = glouton_density(R, C, F, N, B, T, rides, evolutedScore)
    print(solution)
    write(instance+".out", solution)
