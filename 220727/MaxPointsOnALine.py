import numpy as np
import math


def max_n_points(points):
    n_points = len(points)
    count = np.zeros((n_points, n_points))
    n = 0
    for pole in points:
        pars = []
        p = -1
        for point in points:
            p += 1
            if p != n:
                if abs(point[0] - pole[0]) > 1e-6:
                    slope = (point[1] - pole[1]) / (point[0] - pole[0])
                    intercept = point[1] - slope * point[0]
                else:
                    slope = float(math.inf)
                    intercept = pole[0]


                if (slope, intercept) in pars:
                    q = pars.index((slope, intercept))
                    count[n, q] += 1
                else:
                    pars.append((slope, intercept))

        n += 1
    return int(np.amax(count)+2)


count_ = max_n_points(np.array([[0, 0], [2, 0], [3, 0], [0,1], [0,2], [0,3]]))
print(count_)
