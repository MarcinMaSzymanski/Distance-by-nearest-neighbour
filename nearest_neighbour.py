import numpy as np
import random
from utils import timer

@timer
def distance_by_nearest_neighbour(X):
    squared_distance = []
    i = random.randint(0, len(X))
    point = X[i, :]
    X_prim = np.delete(X, i, 0)

    #Calculate distance without root
    euclidean_distance = lambda A, p: (A[:, 0] - p[0]) ** 2 + (A[:, 1] - p[1]) ** 2

    while len(X_prim) != 0:
        distance = euclidean_distance(X_prim, point)
        i = np.argmin(distance)
        squared_distance.append(distance[i])
        point = X_prim[i, :]
        X_prim = np.delete(X_prim, i, 0)

    total_distance = (np.array(squared_distance) ** 0.5).sum()
    print('Total distance connecting points by nearest neighbour: ' + str(total_distance))

