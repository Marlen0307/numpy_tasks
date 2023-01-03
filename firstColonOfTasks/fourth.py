import numpy as np

first_matrix = np.random.random((5, 3))
second_matrix = np.random.random((3, 2))
z = np.dot(first_matrix, second_matrix)
print("Dot product of two matrices:")
print(z)
