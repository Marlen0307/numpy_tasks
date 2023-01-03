import numpy as np

vector = np.random.random((1000, 2))
x, y = np.atleast_2d(vector[:, 0], vector[:, 1])
distances = np.sqrt((x - x.T) ** 2 + (y - y.T) ** 2)
print("Distances array:")
print(distances)
