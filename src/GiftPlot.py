import GrahamScan as gs
import numpy as np
import matplotlib.pyplot as plot

# Helper method to split a set of points containing points (x,y) into
# a set with all x coords and a parallel set with all y coords.
def split_points(point_set):
    x_coords = []
    y_coords = []

    for point in point_set:
        x_coords.append(point[0])
        y_coords.append(point[1])

    return [x_coords, y_coords]

# Example code ... create a gift and its graham scan, then print.
gift = [(1,2),(1,3),(1,4),(2,5)]
isConvex = gs.counter_clockwise(gift[0],gift[1],gift[2])

split_gift = split_points(gift)

plot.scatter(split_gift[0], split_gift[1])
plot.show()

print(isConvex)

# import numpy as np
# import matplotlib.pyplot as plt

# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)

# plt.scatter(x, y)
# plt.show()

# Uses numpy to graphically showcase a gift, 
# along with the generated convex hull. Let's see if we can do it this way.